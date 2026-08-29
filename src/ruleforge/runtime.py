from __future__ import annotations

from dataclasses import dataclass
import fnmatch
import ipaddress
from pathlib import PurePath
from typing import Iterable

from .model import Rule
from .routing import rule_sort_key


@dataclass(frozen=True)
class RouteProbe:
    domain: str | None = None
    ip: str | None = None
    process: str | None = None
    destination_port: int | None = None
    inbound_port: int | None = None


@dataclass(frozen=True)
class RouteResult:
    policy: str
    rule: Rule


def _domain(probe: RouteProbe) -> str | None:
    if probe.domain is None:
        return None
    return probe.domain.casefold().rstrip(".")


def _process_name(value: str | None) -> str | None:
    if not value:
        return None
    return PurePath(value.replace("\\", "/")).name.casefold()


def _port_matches(value: str, port: int | None) -> bool:
    if port is None:
        return False
    try:
        if "-" in value:
            start, end = (int(part) for part in value.split("-", 1))
            return start <= port <= end
        return int(value) == port
    except ValueError:
        return False


def rule_matches(rule: Rule, probe: RouteProbe) -> bool:
    domain = _domain(probe)
    value = rule.value.casefold()
    if rule.rule_type == "HOST":
        return domain == value
    if rule.rule_type == "HOST-SUFFIX":
        return domain == value or (domain is not None and domain.endswith("." + value))
    if rule.rule_type == "HOST-KEYWORD":
        return domain is not None and value in domain
    if rule.rule_type == "HOST-WILDCARD":
        return domain is not None and fnmatch.fnmatchcase(domain, value)
    if rule.rule_type in {"IP-CIDR", "IP6-CIDR"}:
        if probe.ip is None:
            return False
        try:
            return ipaddress.ip_address(probe.ip) in ipaddress.ip_network(rule.value, strict=False)
        except ValueError:
            return False
    if rule.rule_type == "PROCESS-NAME":
        return _process_name(probe.process) == value
    if rule.rule_type == "DEST-PORT":
        return _port_matches(rule.value, probe.destination_port)
    if rule.rule_type == "IN-PORT":
        return _port_matches(rule.value, probe.inbound_port)
    return False


def order_rules_for_first_match(rules: Iterable[Rule]) -> tuple[Rule, ...]:
    """Order rules the same way the generated category outputs are consumed."""

    return tuple(
        sorted(
            rules,
            key=rule_sort_key,
        )
    )


def simulate_route(rules: Iterable[Rule], probe: RouteProbe) -> RouteResult | None:
    for rule in rules:
        if rule_matches(rule, probe):
            return RouteResult(rule.policy, rule)
    return None


def simulate_first_match(rules: Iterable[Rule], probe: RouteProbe) -> RouteResult | None:
    return simulate_route(order_rules_for_first_match(rules), probe)
