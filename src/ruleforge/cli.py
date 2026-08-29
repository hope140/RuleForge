from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import __version__
from .audit import audit_rules, resolve_conflicts
from .curation import curate_rules
from .fetch import FetchError, fetch_source
from .manifest import ManifestError, load_manifest
from .parsers import parse_resource
from .render import (
    render_audit,
    render_category_filters,
    render_conflicts,
    render_filter_remote_conf,
    render_json,
    render_mihomo_category_filters,
    render_mihomo_rule_providers,
    render_mihomo_rules,
)


def _default_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _manifest_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--manifest", default="sources/quantumultx.yaml")


def _lint(args: argparse.Namespace) -> int:
    _, sources = load_manifest(args.manifest)
    enabled = [source for source in sources if source.enabled]
    formats: dict[str, int] = {}
    for source in enabled:
        formats[source.format] = formats.get(source.format, 0) + 1
    print(f"manifest={args.manifest}")
    print(f"sources={len(sources)} enabled={len(enabled)} formats={formats}")
    return 0


def _build(args: argparse.Namespace) -> int:
    manifest_data, sources = load_manifest(args.manifest)
    target = str(manifest_data["target"]).lower()
    if target not in {"quantumult-x", "mihomo"}:
        raise ManifestError(f"unsupported target: {target}")
    output_dir = Path(args.output_dir or f"outputs/{target}")
    cache_dir = Path(args.cache_dir)
    all_rules = []
    parse_issues = []
    fetch_errors = []
    source_metadata = []
    for source in sources:
        if not source.enabled:
            continue
        try:
            resource = fetch_source(
                source,
                cache_dir,
                timeout=args.timeout,
                offline=args.offline,
                refresh=args.refresh,
            )
        except FetchError as exc:
            fetch_errors.append(str(exc))
            continue
        result = parse_resource(resource.text, source)
        all_rules.extend(result.rules)
        parse_issues.extend(issue.to_dict() for issue in result.issues)
        source_metadata.append(
            {
                "id": source.id,
                "url": source.url,
                "sha256": resource.sha256,
                "from_cache": resource.from_cache,
                "rule_count": len(result.rules),
                "issue_count": len(result.issues),
            }
        )

    candidate_audit = audit_rules(all_rules)
    curation = curate_rules(all_rules)
    audit = audit_rules(curation.rules)
    resolution = resolve_conflicts(audit)
    generated_at_utc = datetime.now(timezone.utc).isoformat()
    category_policies: dict[str, str] = {}
    for source in sources:
        if not source.enabled:
            continue
        previous_policy = category_policies.get(source.category)
        if previous_policy is not None and previous_policy != source.policy:
            raise ManifestError(
                f"category {source.category} has mixed policies: "
                f"{previous_policy!r} and {source.policy!r}"
            )
        category_policies[source.category] = source.policy
    if target == "mihomo":
        unsupported = []
        for rule in all_rules:
            try:
                rule.to_mihomo()
            except ValueError:
                unsupported.append(rule)
        if unsupported:
            sample = ", ".join(
                f"{rule.source_id}:{rule.line_number}:{rule.rule_type}" for rule in unsupported[:10]
            )
            print(
                f"error: unsupported Mihomo rules={len(unsupported)} sample={sample}",
                file=sys.stderr,
            )
            return 3

    output_dir.mkdir(parents=True, exist_ok=True)
    category_renderer = (
        render_mihomo_category_filters if target == "mihomo" else render_category_filters
    )
    relative_root = f"outputs/{target}/categories"
    candidate_categories = category_renderer(
        candidate_audit.kept_rules,
        output_dir / "categories" / "candidates",
        generated_at_utc=generated_at_utc,
        relative_prefix=f"{relative_root}/candidates",
        category_policies=category_policies,
    )
    safe_categories = category_renderer(
        resolution.rules,
        output_dir / "categories" / "safe",
        generated_at_utc=generated_at_utc,
        relative_prefix=f"{relative_root}/safe",
        category_policies=category_policies,
    )
    if target == "mihomo":
        render_mihomo_rule_providers(
            safe_categories,
            output_dir / "rule-providers.safe.yaml",
            repository_base_url=args.repository_base_url,
        )
        render_mihomo_rules(safe_categories, output_dir / "rules.safe.yaml")
    else:
        render_filter_remote_conf(
            safe_categories,
            output_dir / "filter_remote.safe.conf",
            repository_base_url=args.repository_base_url,
            title="Resolved category filters (Blackmatrix preferred)",
        )
    render_audit(audit, output_dir / "audit.json", resolution=resolution)
    render_conflicts(audit.conflicts, output_dir / "conflicts.md", resolution=resolution)
    render_json(
        {
            "generated_at_utc": generated_at_utc,
            "generator_version": __version__,
            "manifest": manifest_data,
            "source_count": len(sources),
            "enabled_source_count": len([source for source in sources if source.enabled]),
            "parsed_rule_count": len(all_rules),
            "curated_rule_count": len(curation.rules),
            "curation_drop_count": len(curation.dropped),
            "candidate_kept_rule_count": len(candidate_audit.kept_rules),
            "kept_rule_count": len(audit.kept_rules),
            "safe_rule_count": len(resolution.rules),
            "resolved_rule_count": len(resolution.rules),
            "conflicted_rule_count": len(audit.conflicted_rules),
            "duplicate_count": len(audit.duplicates),
            "conflict_count": len(audit.conflicts),
            "resolved_conflict_count": len(resolution.preferred_decisions),
            "blackmatrix_preferred_conflict_count": len(resolution.blackmatrix_decisions),
            "direct_preferred_conflict_count": len(resolution.direct_decisions),
            "specific_preferred_conflict_count": len(resolution.specific_decisions),
            "category_preferred_conflict_count": len(resolution.category_decisions),
            "protective_reject_conflict_count": len(resolution.protective_reject_decisions),
            "ordered_overlap_count": len(resolution.ordered_overlap_decisions),
            "routing_constraint_count": len(resolution.constraints),
            "unresolved_conflict_count": len(resolution.unresolved_decisions),
            "resolution": resolution.to_summary_dict(),
            "candidate_categories": candidate_categories,
            "safe_categories": safe_categories,
            "parse_issue_count": len(parse_issues),
            "fetch_error_count": len(fetch_errors),
            "sources": source_metadata,
            "parse_issues": parse_issues,
            "fetch_errors": fetch_errors,
        },
        output_dir / "build.json",
    )
    render_json(curation.to_dict(), output_dir / "curation.json")
    print(
        f"sources={len(source_metadata)} parsed_rules={len(all_rules)} "
        f"curated_rules={len(curation.rules)} curation_drops={len(curation.dropped)} "
        f"kept_rules={len(audit.kept_rules)} resolved_rules={len(resolution.rules)}"
    )
    print(
        f"duplicates={len(audit.duplicates)} conflicts={len(audit.conflicts)} "
        f"blackmatrix_preferred={len(resolution.blackmatrix_decisions)} "
        f"direct_preferred={len(resolution.direct_decisions)} "
        f"specific_preferred={len(resolution.specific_decisions)} "
        f"category_preferred={len(resolution.category_decisions)} "
        f"protective_reject={len(resolution.protective_reject_decisions)} "
        f"ordered_overlap={len(resolution.ordered_overlap_decisions)} "
        f"unresolved={len(resolution.unresolved_decisions)} parse_issues={len(parse_issues)}"
    )
    print(f"output={output_dir}")
    if fetch_errors or parse_issues:
        return 1
    if args.fail_on_conflict and resolution.unresolved_decisions:
        return 2
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ruleforge")
    subparsers = parser.add_subparsers(dest="command", required=True)

    lint = subparsers.add_parser("lint", help="validate the source manifest")
    _manifest_arg(lint)
    lint.set_defaults(handler=_lint)

    build = subparsers.add_parser("build", help="fetch, parse, audit and render rules")
    _manifest_arg(build)
    build.add_argument("--output-dir")
    build.add_argument("--cache-dir", default=".cache/ruleforge")
    build.add_argument("--timeout", type=float, default=30.0)
    build.add_argument("--offline", action="store_true")
    build.add_argument("--refresh", action="store_true")
    build.add_argument(
        "--repository-base-url",
        default="https://raw.githubusercontent.com/hope140/RuleForge/main",
        help="base URL used in filter_remote.safe.conf",
    )
    build.add_argument("--fail-on-conflict", action="store_true")
    build.set_defaults(handler=_build)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.handler(args))
    except (ManifestError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
