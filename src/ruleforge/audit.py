from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .model import Rule


@dataclass(frozen=True)
class Duplicate:
    kept: Rule
    dropped: Rule

    def to_dict(self) -> dict[str, object]:
        return {"kept": self.kept.to_dict(), "dropped": self.dropped.to_dict()}


@dataclass(frozen=True)
class Conflict:
    kind: str
    relation: str
    left: Rule
    right: Rule

    def to_dict(self) -> dict[str, object]:
        return {
            "kind": self.kind,
            "relation": self.relation,
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }


@dataclass(frozen=True)
class AuditResult:
    kept_rules: tuple[Rule, ...]
    duplicates: tuple[Duplicate, ...]
    conflicts: tuple[Conflict, ...]

    @property
    def conflicted_rules(self) -> frozenset[Rule]:
        result: set[Rule] = set()
        for conflict in self.conflicts:
            result.add(conflict.left)
            result.add(conflict.right)
        return frozenset(result)

    @property
    def safe_rules(self) -> tuple[Rule, ...]:
        conflicted = self.conflicted_rules
        return tuple(rule for rule in self.kept_rules if rule not in conflicted)

    def to_dict(self) -> dict[str, object]:
        return {
            "kept_rule_count": len(self.kept_rules),
            "safe_rule_count": len(self.safe_rules),
            "conflicted_rule_count": len(self.conflicted_rules),
            "duplicate_count": len(self.duplicates),
            "conflict_count": len(self.conflicts),
            "duplicates": [item.to_dict() for item in self.duplicates],
            "conflicts": [item.to_dict() for item in self.conflicts],
        }


def _parent_domains(value: str) -> Iterable[str]:
    parts = value.split(".")
    for index in range(1, len(parts)):
        yield ".".join(parts[index:])


def audit_rules(rules: Iterable[Rule]) -> AuditResult:
    kept: list[Rule] = []
    duplicates: list[Duplicate] = []
    conflicts: list[Conflict] = []
    exact: dict[tuple[str, str, tuple[str, ...]], Rule] = {}
    for rule in rules:
        previous = exact.get(rule.identity_key)
        if previous is None:
            exact[rule.identity_key] = rule
            kept.append(rule)
            continue
        if previous.policy == rule.policy:
            duplicates.append(Duplicate(previous, rule))
        else:
            conflicts.append(Conflict("exact-policy", "same-rule-different-policy", previous, rule))

    host_exact: dict[str, list[Rule]] = {}
    host_suffix: dict[str, list[Rule]] = {}
    for rule in kept:
        if rule.rule_type == "HOST":
            host_exact.setdefault(rule.value, []).append(rule)
        elif rule.rule_type == "HOST-SUFFIX":
            host_suffix.setdefault(rule.value, []).append(rule)

    seen_pairs: set[tuple[int, int, str]] = set()

    def add_overlap(left: Rule, right: Rule, relation: str) -> None:
        if left.policy == right.policy:
            return
        pair = (id(left), id(right), relation)
        reverse = (id(right), id(left), relation)
        if pair in seen_pairs or reverse in seen_pairs:
            return
        seen_pairs.add(pair)
        conflicts.append(Conflict("semantic-overlap", relation, left, right))

    for value, exact_rules in host_exact.items():
        for suffix in (value, *_parent_domains(value)):
            for suffix_rule in host_suffix.get(suffix, []):
                for exact_rule in exact_rules:
                    add_overlap(exact_rule, suffix_rule, "host-inside-host-suffix")

    suffix_values = sorted(host_suffix)
    for index, left_value in enumerate(suffix_values):
        for right_value in suffix_values[index + 1 :]:
            if left_value.endswith("." + right_value):
                for left in host_suffix[left_value]:
                    for right in host_suffix[right_value]:
                        add_overlap(left, right, "nested-host-suffix")
            elif right_value.endswith("." + left_value):
                for left in host_suffix[left_value]:
                    for right in host_suffix[right_value]:
                        add_overlap(left, right, "nested-host-suffix")

    return AuditResult(tuple(kept), tuple(duplicates), tuple(conflicts))
