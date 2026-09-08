"""Hungarian occupancy-informed alignment demo using packaged data/ paths.

Run from the Github package root:
  python code/hungarian_alignment_demo.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.optimize import linear_sum_assignment

ROOT = Path(__file__).resolve().parents[1]
LUNA = ROOT / "data/occupancy/luna/occupancy_summary_k4.json"
OUR = ROOT / "data/occupancy/our/occupancy_summary_k4.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def occ_means(summary: dict, group: str, k: int = 4) -> np.ndarray:
    return np.array([summary[group][f"occupancy_state_{i}_mean"] for i in range(k)])


def cos_dist(a, b):
    a = a / (np.linalg.norm(a) + 1e-12)
    b = b / (np.linalg.norm(b) + 1e-12)
    return 1.0 - float(a @ b)


def hungarian_perm(ln, le, un, ue):
    k = len(ln)
    cost = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            cost[i, j] = cos_dist(np.array([ln[i], le[i]]), np.array([un[j], ue[j]]))
    r, c = linear_sum_assignment(cost)
    return c[np.argsort(r)], cost


def main():
    luna, our = load(LUNA), load(OUR)
    ln, le = occ_means(luna, "non-epilepsy"), occ_means(luna, "epilepsy")
    un, ue = occ_means(our, "non-epilepsy"), occ_means(our, "epilepsy")
    perm, cost = hungarian_perm(ln, le, un, ue)
    luna_d = 100 * (le - ln)
    our_d = 100 * (ue - un)
    r = float(np.corrcoef(luna_d, our_d[perm])[0, 1])

    print("Occupancy-informed Hungarian (k=4)")
    print("perm[i] = OUR state matched to LUNA state i:", perm.tolist())
    print("LUNA Delta occ (%):", np.round(luna_d, 2))
    print("OUR  Delta occ aligned (%):", np.round(our_d[perm], 2))
    print(f"r_Delta = {r:.4f}")
    print("cost matrix (cosine distance):\n", np.round(cost, 4))


if __name__ == "__main__":
    main()
