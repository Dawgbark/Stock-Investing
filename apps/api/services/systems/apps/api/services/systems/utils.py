"""Utilities for deterministic stub data."""

from __future__ import annotations

import hashlib
from typing import Iterable, List


def stable_ratio(*parts: str) -> float:
    """Return a stable ratio in [0, 1] based on the provided parts."""
    joined = ":".join(parts)
    digest = hashlib.sha256(joined.encode("utf-8")).hexdigest()
    return int(digest[:8], 16) / 0xFFFFFFFF


def stable_range(min_value: float, max_value: float, *parts: str) -> float:
    ratio = stable_ratio(*parts)
    return min_value + (max_value - min_value) * ratio


def stable_choice(options: Iterable[str], *parts: str) -> str:
    options_list: List[str] = list(options)
    if not options_list:
        raise ValueError("options must not be empty")
    index = int(stable_ratio(*parts) * len(options_list))
    return options_list[min(index, len(options_list) - 1)]
