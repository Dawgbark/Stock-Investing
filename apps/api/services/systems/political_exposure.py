"""Stub political exposure insights."""

from __future__ import annotations

from typing import Dict, List

from .utils import stable_choice, stable_range


SECTORS = ("technology", "energy", "finance", "healthcare", "industrials")


def get_political_exposure(ticker: str) -> Dict[str, object]:
    """Return a deterministic political exposure payload."""
    normalized = ticker.upper().strip()
    risk_score = round(stable_range(15, 70, "policy-risk", normalized), 1)
    confidence = round(stable_range(0.2, 0.6, "policy-confidence", normalized), 2)
    sector = stable_choice(SECTORS, "policy-sector", normalized)
    mentions: List[Dict[str, str]] = [
        {
            "source": "Hearing transcript",
            "summary": f"${normalized} referenced in context of {sector} oversight.",
        },
        {
            "source": "Regulatory briefing",
            "summary": f"Potential policy watch items tied to {sector} industry trends.",
        },
    ]

    return {
        "risk_score": risk_score,
        "confidence": confidence,
        "sector": sector,
        "mentions": mentions,
        "notes": "Synthetic placeholders until real policy ingestion is wired up.",
    }
