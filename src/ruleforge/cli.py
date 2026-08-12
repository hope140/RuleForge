from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

from .audit import audit_rules
from .fetch import FetchError, fetch_source
from .manifest import ManifestError, load_manifest
from .parsers import parse_resource
from .render import (
    render_audit,
    render_category_filters,
    render_conflicts,
    render_filter_remote_conf,
    render_json,
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
    output_dir = Path(args.output_dir)
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

    audit = audit_rules(all_rules)
    generated_at_utc = datetime.now(timezone.utc).isoformat()
    output_dir.mkdir(parents=True, exist_ok=True)
    candidate_categories = render_category_filters(
        audit.kept_rules,
        output_dir / "categories" / "candidates",
        generated_at_utc=generated_at_utc,
        relative_prefix="outputs/quantumult-x/categories/candidates",
    )
    safe_categories = render_category_filters(
        audit.safe_rules,
        output_dir / "categories" / "safe",
        generated_at_utc=generated_at_utc,
        relative_prefix="outputs/quantumult-x/categories/safe",
    )
    render_filter_remote_conf(
        safe_categories,
        output_dir / "filter_remote.safe.conf",
        repository_base_url=args.repository_base_url,
        title="Conservative category filters",
    )
    render_audit(audit, output_dir / "audit.json")
    render_conflicts(audit.conflicts, output_dir / "conflicts.md")
    render_json(
        {
            "generated_at_utc": generated_at_utc,
            "generator_version": "0.1.0",
            "manifest": manifest_data,
            "source_count": len(sources),
            "enabled_source_count": len([source for source in sources if source.enabled]),
            "parsed_rule_count": len(all_rules),
            "kept_rule_count": len(audit.kept_rules),
            "safe_rule_count": len(audit.safe_rules),
            "conflicted_rule_count": len(audit.conflicted_rules),
            "duplicate_count": len(audit.duplicates),
            "conflict_count": len(audit.conflicts),
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
    print(
        f"sources={len(source_metadata)} parsed_rules={len(all_rules)} "
        f"kept_rules={len(audit.kept_rules)} safe_rules={len(audit.safe_rules)}"
    )
    print(f"duplicates={len(audit.duplicates)} conflicts={len(audit.conflicts)} parse_issues={len(parse_issues)}")
    print(f"output={output_dir}")
    if fetch_errors:
        return 1
    if args.fail_on_conflict and audit.conflicts:
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
    build.add_argument("--output-dir", default="outputs/quantumult-x")
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
