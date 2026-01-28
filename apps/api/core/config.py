"""Application configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Configuration settings loaded from environment variables."""

    environment: str = os.getenv("APP_ENV", "development")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    cache_ttl_seconds: int = int(os.getenv("CACHE_TTL_SECONDS", "300"))


def get_settings() -> Settings:
    """Return settings for the current environment."""
    return Settings()
