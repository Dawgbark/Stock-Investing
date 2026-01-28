"""Stub Google Trends signal."""

from __future__ import annotations

from datetime import date
from typing import Dict, List

from .utils import stable_range


def _month_labels(months: int) -> List[str]:
    today = date.today()
    labels: List[str] = []
    year = today.year
    month = today.month
    for _ in range(months):
        labels.append(f"{year}-{month:02d}")
        month -= 1
        if month == 0:
            month = 12
            year -= 1
    return list(reversed(labels))


def get_google_trends(ticker: str) -> Dict[str, object]:
    """Return a deterministic trends payload."""
    normalized = ticker.upper().strip()
    baseline = round(stable_range(25, 55, "trends-baseline", normalized), 1)
    recent = round(stable_range(35, 75, "trends-recent", normalized), 1)

    labels = _month_labels(12)
    series = [
        {
            "month": label,
            "interest": round(
                stable_range(20, 90, "trends", normalized, label), 1
            ),
        }
        for label in labels
    ]

    return {
        "baseline": baseline,
        "recent": recent,
        "delta": round(recent - baseline, 1),
        "series": series,
        "notes": "Synthetic trend line built from deterministic seed.",
    }
