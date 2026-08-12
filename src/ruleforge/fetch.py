from __future__ import annotations

import hashlib
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from .model import Source


class FetchError(RuntimeError):
    pass


@dataclass(frozen=True)
class FetchedResource:
    source: Source
    text: str
    sha256: str
    from_cache: bool


def _cache_path(cache_dir: Path, url: str) -> Path:
    key = hashlib.sha256(url.encode("utf-8")).hexdigest()[:24]
    return cache_dir / f"{key}.txt"


def fetch_source(
    source: Source,
    cache_dir: str | Path,
    *,
    timeout: float = 30.0,
    offline: bool = False,
    refresh: bool = False,
    max_bytes: int = 25 * 1024 * 1024,
) -> FetchedResource:
    cache_path = _cache_path(Path(cache_dir), source.url)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    if cache_path.exists() and not refresh:
        raw = cache_path.read_bytes()
        return FetchedResource(source, raw.decode("utf-8-sig", errors="replace"), hashlib.sha256(raw).hexdigest(), True)
    if offline:
        raise FetchError(f"offline cache miss: {source.id}")
    request = urllib.request.Request(source.url, headers={"User-Agent": "RuleForge/0.1"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = getattr(response, "status", 200)
            if status != 200:
                raise FetchError(f"{source.id}: HTTP {status}")
            raw = response.read(max_bytes + 1)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise FetchError(f"{source.id}: {exc}") from exc
    if len(raw) > max_bytes:
        raise FetchError(f"{source.id}: response exceeds {max_bytes} bytes")
    cache_path.write_bytes(raw)
    return FetchedResource(source, raw.decode("utf-8-sig", errors="replace"), hashlib.sha256(raw).hexdigest(), False)
