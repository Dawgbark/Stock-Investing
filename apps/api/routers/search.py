"""Search helpers for tickers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List


DEFAULT_RESULTS: List[Dict[str, str]] = [
    {"ticker": "AAPL", "name": "Apple Inc.", "exchange": "NASDAQ"},
    {"ticker": "MSFT", "name": "Microsoft Corp.", "exchange": "NASDAQ"},
    {"ticker": "GOOGL", "name": "Alphabet Inc.", "exchange": "NASDAQ"},
    {"ticker": "AMZN", "name": "Amazon.com Inc.", "exchange": "NASDAQ"},
    {"ticker": "TSLA", "name": "Tesla Inc.", "exchange": "NASDAQ"},
]


def _load_dataset() -> List[Dict[str, str]]:
    search_path = Path(__file__).resolve().parents[3] / "Search"
    if not search_path.exists():
        return DEFAULT_RESULTS
    try:
        payload = json.loads(search_path.read_text())
    except json.JSONDecodeError:
        return DEFAULT_RESULTS
    results = payload.get("results") if isinstance(payload, dict) else None
    if isinstance(results, list):
        return [result for result in results if isinstance(result, dict)]
    return DEFAULT_RESULTS


def search_tickers(query: str) -> Dict[str, object]:
    """Search ticker records with a simple contains filter."""
    normalized = (query or "").strip().lower()
    dataset = _load_dataset()
    if not normalized:
        return {"query": query, "results": dataset}

    filtered = [
        entry
        for entry in dataset
        if normalized in entry.get("ticker", "").lower()
        or normalized in entry.get("name", "").lower()
    ]
    return {"query": query, "results": filtered}
