from __future__ import annotations

import hashlib
import json
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from .model import Source
from .magicrule import resolve_resource


class FetchError(RuntimeError):
    pass


@dataclass(frozen=True)
class FetchedResource:
    source: Source
    text: str
    sha256: str
    from_cache: bool
    resolved_url: str = ""


def _cache_path(cache_dir: Path, url: str) -> Path:
    key = hashlib.sha256(url.encode("utf-8")).hexdigest()[:24]
    return cache_dir / f"{key}.txt"


def _download(url: str, source_id: str, timeout: float, max_bytes: int, attempts: int) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "RuleForge/0.1"})
    last_error: BaseException | None = None
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                status = getattr(response, "status", 200)
                if status != 200:
                    raise FetchError(f"{source_id}: HTTP {status}")
                raw = response.read(max_bytes + 1)
            if len(raw) > max_bytes:
                raise FetchError(f"{source_id}: response exceeds {max_bytes} bytes")
            return raw
        except urllib.error.HTTPError as exc:
            if 400 <= exc.code < 500:
                raise FetchError(f"{source_id}: HTTP {exc.code}") from exc
            last_error = exc
        except FetchError:
            raise
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_error = exc
        if attempt + 1 < attempts:
            time.sleep(2**attempt)
    raise FetchError(f"{source_id}: {last_error}") from last_error


def fetch_source(
    source: Source,
    cache_dir: str | Path,
    *,
    timeout: float = 30.0,
    offline: bool = False,
    refresh: bool = False,
    max_bytes: int = 25 * 1024 * 1024,
    attempts: int = 3,
    metadata_cache: dict[str, bytes] | None = None,
) -> FetchedResource:
    if source.url.startswith("inline:"):
        raw = source.url.removeprefix("inline:").encode("utf-8")
        return FetchedResource(
            source,
            raw.decode("utf-8"),
            hashlib.sha256(raw).hexdigest(),
            True,
        )
    cache_path = _cache_path(Path(cache_dir), source.url)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    if cache_path.exists() and not refresh:
        raw = cache_path.read_bytes()
        metadata_path = cache_path.with_suffix(".json")
        resolved_url = ""
        if source.resolver and metadata_path.exists():
            try:
                metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
                if metadata.get("sha256") == hashlib.sha256(raw).hexdigest():
                    resolved_url = metadata.get("resolved_url", "")
            except (ValueError, AttributeError):
                pass
        return FetchedResource(source, raw.decode("utf-8-sig", errors="replace"), hashlib.sha256(raw).hexdigest(), True, resolved_url)
    if offline:
        raise FetchError(f"offline cache miss: {source.id}")
    if attempts < 1:
        raise ValueError("attempts must be at least 1")
    resolved_url = source.url
    if source.resolver == "magicrule":
        try:
            raw, resolved_url = resolve_resource(
                source, lambda url: _download(url, source.id, timeout, max_bytes, attempts),
                metadata_cache if metadata_cache is not None else {},
            )
        except (ValueError, KeyError, TypeError, AttributeError) as exc:
            raise FetchError(f"{source.id}: {exc}") from exc
    else:
        raw = _download(source.url, source.id, timeout, max_bytes, attempts)
    cache_path.write_bytes(raw)
    sha256 = hashlib.sha256(raw).hexdigest()
    if source.resolver:
        cache_path.with_suffix(".json").write_text(
            json.dumps({"resolved_url": resolved_url, "sha256": sha256}), encoding="utf-8",
        )
    return FetchedResource(source, raw.decode("utf-8-sig", errors="replace"), sha256, False, resolved_url)
