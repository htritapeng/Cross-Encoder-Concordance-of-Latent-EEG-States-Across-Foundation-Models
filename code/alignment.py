"""Hungarian alignment utilities for cross-encoder latent-state concordance."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.optimize import linear_sum_assignment


def load_occupancy_summary(path: Path | str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def occupancy_means(summary: dict, group: str, k: int) -> np.ndarray:
    """group is 'non-epilepsy' or 'epilepsy'."""
    return np.array(
        [float(summary[group][f"occupancy_state_{i}_mean"]) for i in range(k)],
        dtype=float,
    )


def cosine_distance(a: np.ndarray, b: np.ndarray) -> float:
    a = a / (np.linalg.norm(a) + 1e-12)
    b = b / (np.linalg.norm(b) + 1e-12)
    return 1.0 - float(a @ b)


def hungarian_occupancy_informed(
    luna_nonepi: np.ndarray,
    luna_epi: np.ndarray,
    our_nonepi: np.ndarray,
    our_epi: np.ndarray,
) -> np.ndarray:
    """Match OUR states to LUNA using f_i = (NonEpi, Epi) cosine distance.

    Returns perm where OUR state perm[i] is matched to LUNA state i.
    """
    k = len(luna_nonepi)
    cost = np.zeros((k, k), dtype=float)
    for i in range(k):
        for j in range(k):
            cost[i, j] = cosine_distance(
                np.array([luna_nonepi[i], luna_epi[i]]),
                np.array([our_nonepi[j], our_epi[j]]),
            )
    rows, cols = linear_sum_assignment(cost)
    return cols[np.argsort(rows)]


def delta_occupancy(epi: np.ndarray, nonepi: np.ndarray) -> np.ndarray:
    return epi - nonepi


def concordance_r_delta(luna_delta: np.ndarray, our_delta_aligned: np.ndarray) -> float:
    return float(np.corrcoef(luna_delta, our_delta_aligned)[0, 1])


def hungarian_coassignment(contingency: np.ndarray) -> np.ndarray:
    """Maximize co-assignment counts (label-independent). contingency[i, j] = count(LUNA=i, OUR=j)."""
    rows, cols = linear_sum_assignment(-contingency)
    return cols[np.argsort(rows)]
