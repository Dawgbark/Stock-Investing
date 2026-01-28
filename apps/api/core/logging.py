"""Logging helpers."""

from __future__ import annotations

import logging

from .config import get_settings


def configure_logging() -> None:
    """Configure logging for the application."""
    settings = get_settings()
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger instance."""
    configure_logging()
    return logging.getLogger(name)
