from __future__ import annotations

import hashlib
import json
from collections.abc import Callable
from urllib.parse import unquote, urldefrag, urlsplit

from .model import Source


def resolve_resource(
    source: Source,
    download: Callable[[str], bytes],
    metadata_cache: dict[str, bytes],
) -> tuple[bytes, str]:
    """Resolve the current artifact on every refresh, rather than pinning its hash."""

    def document(url: str) -> dict:
        if url not in metadata_cache:
            metadata_cache[url] = download(url)
        value = json.loads(metadata_cache[url].decode("utf-8-sig"))
        if not isinstance(value, dict):
            raise ValueError("MagicRule metadata must be an object")
        return value

    def public_url(url: object, prefix: str) -> str:
        if not isinstance(url, str):
            raise ValueError("MagicRule download URL is missing")
        parts = urlsplit(url)
        # The official index also distributes files across other pages.dev shards.
        if (parts.scheme != "https" or not (parts.hostname or "").endswith(".pages.dev")
                or parts.username or parts.password or parts.port not in {None, 443}
                or not parts.path.startswith(prefix) or parts.query or parts.fragment):
            raise ValueError(f"invalid MagicRule download URL: {url}")
        return url

    index_url, name = urldefrag(source.url)
    client = "QuantumultX" if source.format == "quantumult-x" else "Mihomo"
    index = document(index_url)
    if index.get("client") != client or not isinstance(index.get("rules"), list):
        raise ValueError("MagicRule client index does not match the source format")
    matches = [rule for rule in index["rules"]
               if isinstance(rule, dict) and rule.get("name") == unquote(name)]
    if len(matches) != 1:
        raise ValueError(f"MagicRule category must exist exactly once: {unquote(name)}")
    manifest = document(public_url(matches[0].get("manifest"), f"/data/rules/{client}/"))
    if manifest.get("client") != client or manifest.get("rule") != unquote(name):
        raise ValueError("MagicRule manifest does not match the requested category")
    key = "rules" if client == "QuantumultX" else "classical"
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list):
        raise ValueError("MagicRule manifest has no artifacts")
    matches = [a for a in artifacts if isinstance(a, dict) and a.get("key") == key
               and a.get("binary") is False and a.get("empty") is False]
    if len(matches) != 1:
        raise ValueError(f"MagicRule requires exactly one nonempty {key} text artifact")
    artifact = matches[0]
    url = public_url(artifact.get("url"), "/data/_shared/artifacts/")
    raw = download(url)
    dedupe = artifact.get("dedupe") or {}
    expected = dedupe.get("bytes_sha256")
    if expected and hashlib.sha256(raw).hexdigest() != expected:
        # Shared artifacts may retain another generation's four comment
        # headers. The manifest documents a separate digest for this body.
        lines = raw.decode("utf-8-sig").splitlines()
        headers = ("# NAME:", "# AUTHOR:", "# REPO:", "# UPDATED:")
        normalized = dedupe.get("mode") == "standard_header_normalized" and dedupe.get("normalized_header_lines") == 4
        standard_header = len(lines) >= 4 and all(line.startswith(prefix) for line, prefix in zip(lines, headers))
        semantic = dedupe.get("semantic_sha256")
        body = ("\n".join(lines[4:]) + "\n").encode("utf-8")
        if not (normalized and standard_header and semantic and hashlib.sha256(body).hexdigest() == semantic):
            raise ValueError("MagicRule artifact SHA256 does not match its manifest")
    if not raw.strip() or raw.lstrip().startswith(b"<"):
        raise ValueError("MagicRule artifact is empty or HTML")
    raw.decode("utf-8-sig")
    return raw, url
