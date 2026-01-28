"""Health check helpers."""

from __future__ import annotations

from datetime import datetime
from typing import Dict


def get_health() -> Dict[str, str]:
    """Return a basic health payload."""
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
