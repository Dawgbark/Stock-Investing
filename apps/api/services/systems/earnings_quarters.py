"""Stub earnings and quarterly performance data."""

from __future__ import annotations

from typing import Dict, List

from .utils import stable_range


def _quarter_label(index: int) -> str:
    year = 2024 - (index // 4)
    quarter = 4 - (index % 4)
    return f"{year} Q{quarter}"


def get_earnings_quarters(ticker: str) -> Dict[str, object]:
    """Return a deterministic earnings history payload."""
    normalized = ticker.upper().strip()
    history: List[Dict[str, object]] = []
    beats = 0
    for index in range(8):
        quarter = _quarter_label(index)
        eps_est = round(stable_range(0.8, 2.4, "eps-est", normalized, quarter), 2)
        eps_act = round(
            eps_est + stable_range(-0.2, 0.35, "eps-act", normalized, quarter), 2
        )
        rev_est = round(stable_range(8, 30, "rev-est", normalized, quarter), 2)
        rev_act = round(
            rev_est + stable_range(-2, 3.5, "rev-act", normalized, quarter), 2
        )
        result = "beat" if eps_act >= eps_est and rev_act >= rev_est else "miss"
        beats += 1 if result == "beat" else 0
        history.append(
            {
                "quarter": quarter,
                "eps_actual": eps_act,
                "eps_estimate": eps_est,
                "revenue_actual": rev_act,
                "revenue_estimate": rev_est,
                "result": result,
            }
        )

    latest = history[0]
    beat_rate = round(beats / len(history), 2)

    return {
        "latest_quarter": latest["quarter"],
        "latest_eps": latest["eps_actual"],
        "latest_revenue": latest["revenue_actual"],
        "beat_rate": beat_rate,
        "history": history,
        "notes": "Synthetic earnings history based on deterministic seed.",
    }
