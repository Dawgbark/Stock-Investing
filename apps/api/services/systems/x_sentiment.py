"""Stub X (Twitter) sentiment analysis."""

from __future__ import annotations

from typing import Dict, List

from .utils import stable_choice, stable_range

SENTIMENT_LABELS = ("bullish", "neutral", "bearish")


def get_x_sentiment(ticker: str) -> Dict[str, object]:
    """Return a deterministic sentiment payload for a ticker."""
    normalized = ticker.upper().strip()
    score = round(stable_range(20, 90, "x", normalized), 1)
    label = stable_choice(SENTIMENT_LABELS, "x-label", normalized)
    mention_volume = {
        "24h": int(stable_range(120, 1800, "x-24h", normalized)),
        "7d": int(stable_range(600, 9000, "x-7d", normalized)),
        "30d": int(stable_range(2400, 42000, "x-30d", normalized)),
    }
    themes = [
        stable_choice(["earnings", "product launch", "guidance"], "x-theme-1", normalized),
        stable_choice(["AI", "cloud", "consumer demand"], "x-theme-2", normalized),
        stable_choice(["margin", "competition", "buyback"], "x-theme-3", normalized),
    ]
    example_posts: List[Dict[str, str]] = [
        {
            "author": "@marketpulse",
            "snippet": f"${normalized} chatter turning {label} after the latest update.",
        },
        {
            "author": "@trendwatch",
            "snippet": f"Mentions of ${normalized} spiked around earnings expectations.",
        },
    ]

    return {
        "score": score,
        "label": label,
        "mention_volume": mention_volume,
        "top_themes": themes,
        "example_posts": example_posts,
        "notes": "Synthetic sample based on deterministic seed.",
    }
