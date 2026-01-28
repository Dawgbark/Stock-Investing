
"""Simple in-memory cache for demo usage."""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any, Dict, Optional


class Cache:
    """A lightweight TTL cache for local development."""

    def __init__(self) -> None:
        self._store: Dict[str, Dict[str, Any]] = {}

    def get(self, key: str) -> Optional[Any]:
        entry = self._store.get(key)
        if not entry:
            return None
        if entry["expires_at"] < datetime.utcnow():
            self._store.pop(key, None)
            return None
        return entry["value"]

    def set(self, key: str, value: Any, ttl_seconds: int = 300) -> None:
        self._store[key] = {
            "value": value,
            "expires_at": datetime.utcnow() + timedelta(seconds=ttl_seconds),
        }

    def clear(self) -> None:
        self._store.clear()
