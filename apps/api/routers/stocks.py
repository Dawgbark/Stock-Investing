"""Stock detail helpers."""

from __future__ import annotations

from typing import Dict

from ..services.evaluator.orchestrator import TickerValidationError, evaluate_ticker


def get_stock_detail(ticker: str) -> Dict[str, object]:
    """Return the multi-system evaluation for a ticker."""
    try:
        return evaluate_ticker(ticker)
    except TickerValidationError as exc:
        return {"error": str(exc)}
