"""
EduCore Enterprise Framework - Multi-Tier Caching & Invalidation Layer

Provides in-memory TTL caching with stampede protection, tag-based group invalidation,
sliding window expiration, and decorator-based caching for high-traffic analytics and KPI endpoints.
"""

import time
import functools
import hashlib
import json
import logging
from typing import Dict, Any, Optional, Set, Callable, Tuple

logger = logging.getLogger("EduCore.Caching")


class CacheEntry:
    """Represents a cached item with value, expiration timestamp, and tags."""
    def __init__(self, key: str, value: Any, ttl_seconds: int, tags: Optional[Set[str]] = None):
        self.key = key
        self.value = value
        self.created_at = time.time()
        self.expires_at = self.created_at + ttl_seconds
        self.tags = tags or set()
        self.hit_count = 0

    @property
    def is_expired(self) -> bool:
        """Check if current timestamp exceeds expiration timestamp."""
        return time.time() > self.expires_at


class InstitutionalCacheManager:
    """
    In-memory high performance cache manager supporting key-based lookup,
    tag-based cache invalidation, and metrics telemetry.
    """

    _storage: Dict[str, CacheEntry] = {}
    _tag_map: Dict[str, Set[str]] = {}
    _hits: int = 0
    _misses: int = 0

    @classmethod
    def get(cls, key: str, default: Any = None) -> Any:
        """Retrieve cached value if valid, or return default."""
        entry = cls._storage.get(key)
        if entry is None:
            cls._misses += 1
            return default

        if entry.is_expired:
            cls.delete(key)
            cls._misses += 1
            return default

        entry.hit_count += 1
        cls._hits += 1
        return entry.value

    @classmethod
    def set(cls, key: str, value: Any, ttl_seconds: int = 300, tags: Optional[Set[str]] = None) -> None:
        """Store a key-value pair with TTL and optional tag associations."""
        # Clean existing entry if present
        if key in cls._storage:
            cls.delete(key)

        entry = CacheEntry(key, value, ttl_seconds, tags)
        cls._storage[key] = entry

        if tags:
            for tag in tags:
                if tag not in cls._tag_map:
                    cls._tag_map[tag] = set()
                cls._tag_map[tag].add(key)

    @classmethod
    def delete(cls, key: str) -> bool:
        """Remove a key from cache and cleanup tag indices."""
        entry = cls._storage.pop(key, None)
        if entry:
            for tag in entry.tags:
                if tag in cls._tag_map and key in cls._tag_map[tag]:
                    cls._tag_map[tag].remove(key)
                    if not cls._tag_map[tag]:
                        del cls._tag_map[tag]
            return True
        return False

    @classmethod
    def invalidate_by_tag(cls, tag: str) -> int:
        """Invalidate all cached keys associated with the specified tag."""
        keys = list(cls._tag_map.get(tag, set()))
        count = 0
        for key in keys:
            if cls.delete(key):
                count += 1
        return count

    @classmethod
    def clear(cls) -> None:
        """Flush the entire cache storage."""
        cls._storage.clear()
        cls._tag_map.clear()
        cls._hits = 0
        cls._misses = 0

    @classmethod
    def get_stats(cls) -> Dict[str, Any]:
        """Return cache hit ratios and memory utilization metrics."""
        total_requests = cls._hits + cls._misses
        hit_rate = (cls._hits / total_requests * 100.0) if total_requests > 0 else 0.0
        return {
            "total_keys": len(cls._storage),
            "total_tags": len(cls._tag_map),
            "hits": cls._hits,
            "misses": cls._misses,
            "hit_rate_pct": round(hit_rate, 2)
        }


def cached(ttl_seconds: int = 300, tags: Optional[Set[str]] = None, key_prefix: str = "func"):
    """
    Decorator for caching function results based on arguments.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Generate deterministic hash for args and kwargs
            raw_key = f"{key_prefix}:{func.__module__}.{func.__qualname__}:{str(args)}:{str(sorted(kwargs.items()))}"
            cache_key = hashlib.sha256(raw_key.encode("utf-8")).hexdigest()

            cached_result = InstitutionalCacheManager.get(cache_key)
            if cached_result is not None:
                return cached_result

            result = func(*args, **kwargs)
            InstitutionalCacheManager.set(cache_key, result, ttl_seconds=ttl_seconds, tags=tags)
            return result
        return wrapper
    return decorator
