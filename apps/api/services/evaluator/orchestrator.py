"""Aggregate system scores into a single evaluation payload."""

from __future__ import annotations

from datetime import datetime
from typing import Dict

from ..systems.earnings_quarters import get_earnings_quarters
from ..systems.google_trends import get_google_trends
from ..systems.political_exposure import get_political_exposure
from ..systems.sp500_relative import get_sp500_relative
from ..systems.x_sentiment import get_x_sentiment

class TickerValidationError(ValueError):
    """Raised when a ticker symbol is invalid."""


def validate_ticker(ticker: str) -> str:
    """Validate and normalize a ticker symbol."""
    if not ticker:
        raise TickerValidationError("Ticker is required.")
    normalized = ticker.strip().upper()
    if not normalized.isalpha() or len(normalized) > 5:
        raise TickerValidationError("Ticker must be 1-5 alphabetic characters.")
    return normalized


def _score_from_trends(trends: Dict[str, object]) -> float:
    baseline = float(trends["baseline"])
    recent = float(trends["recent"])
    delta = max(min(recent - baseline, 50), -50)
    return round(50 + delta, 1)


def _score_from_earnings(earnings: Dict[str, object]) -> float:
    beat_rate = float(earnings["beat_rate"])
    return round(40 + beat_rate * 60, 1)


def _score_from_relative(relative: Dict[str, object]) -> float:
    windows = relative["windows"]
    avg_relative = sum(window["relative_return"] for window in windows) / len(windows)
    return round(50 + avg_relative * 100, 1)


def _score_from_policy(policy: Dict[str, object]) -> float:
    risk = float(policy["risk_score"])
    return round(100 - risk, 1)


def evaluate_ticker(ticker: str) -> Dict[str, object]:
    """Return the full multi-system evaluation payload."""
    normalized = validate_ticker(ticker)

    x_sentiment = get_x_sentiment(normalized)
    trends = get_google_trends(normalized)
    policy = get_political_exposure(normalized)
    relative = get_sp500_relative(normalized)
    earnings = get_earnings_quarters(normalized)

    system_scores = {
        "x_sentiment": {
            "score": x_sentiment["score"],
            "details": x_sentiment,
        },
        "google_trends": {
            "score": _score_from_trends(trends),
            "details": trends,
        },
        "political_exposure": {
            "score": _score_from_policy(policy),
            "details": policy,
        },
        "sp500_relative": {
            "score": _score_from_relative(relative),
            "details": relative,
        },
        "earnings_quarters": {
            "score": _score_from_earnings(earnings),
            "details": earnings,
        },
    }

    composite_score = round(
        sum(item["score"] for item in system_scores.values()) / len(system_scores),
        1,
    )

    return {
        "ticker": normalized,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "composite_score": composite_score,
        "systems": system_scores,
    }
