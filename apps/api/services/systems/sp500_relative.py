"""Stub S&P 500 relative performance calculations."""

from __future__ import annotations

from typing import Dict, List

from .utils import stable_range


WINDOWS = ("1M", "3M", "6M", "1Y", "5Y")


def _window_return(ticker: str, window: str, min_value: float, max_value: float) -> float:
    return round(stable_range(min_value, max_value, "rel", ticker, window), 2)


def get_sp500_relative(ticker: str) -> Dict[str, object]:
    """Return deterministic relative performance windows."""
    normalized = ticker.upper().strip()
    windows: List[Dict[str, float]] = []
    for window in WINDOWS:
        stock_return = _window_return(normalized, window, -0.2, 0.4)
        sp_return = _window_return("SP500", window, -0.1, 0.25)
        windows.append(
            {
                "window": window,
                "stock_return": stock_return,
                "sp500_return": sp_return,
                "relative_return": round(stock_return - sp_return, 2),
            }
        )

    return {
        "windows": windows,
        "alpha": round(stable_range(-0.05, 0.12, "alpha", normalized), 3),
        "beta": round(stable_range(0.8, 1.5, "beta", normalized), 2),
        "notes": "Synthetic performance based on deterministic seed.",
    }
