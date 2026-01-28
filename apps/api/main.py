"""Entry point helpers for the stock analysis API."""

from __future__ import annotations

from typing import Dict

from .routers.health import get_health
from .routers.search import search_tickers
from .routers.stocks import get_stock_detail


def health() -> Dict[str, str]:
    """Return service health payload."""
    return get_health()


def search(query: str) -> Dict[str, object]:
    """Search tickers by query string."""
    return search_tickers(query)


def stock_detail(ticker: str) -> Dict[str, object]:
    """Return details for a ticker symbol."""
    return get_stock_detail(ticker)
