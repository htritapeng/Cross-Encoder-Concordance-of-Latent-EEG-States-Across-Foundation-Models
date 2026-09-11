"""
Demo: occupancy-informed Hungarian alignment and r_Delta (paper primary analysis).

This demo does NOT require frozen model weights. It uses precomputed occupancy
summaries under data/input/occupancy/.

Run from the repository root:
  python demo/run_occupancy_concordance_demo.py
  python demo/run_occupancy_concordance_demo.py --k 5
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from alignment import (  # noqa: E402
    concordance_r_delta,
    delta_occupancy,
    hungarian_occupancy_informed,
    load_occupancy_summary,
    occupancy_means,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Cross-encoder occupancy concordance demo")
    parser.add_argument("--k", type=int, default=4, choices=[3, 4, 5], help="number of states")
    args = parser.parse_args()
    k = args.k

    luna_path = ROOT / "data/input/occupancy/luna" / f"occupancy_summary_k{k}.json"
    our_path = ROOT / "data/input/occupancy/our" / f"occupancy_summary_k{k}.json"
    if not luna_path.exists() or not our_path.exists():
        raise FileNotFoundError(
            f"Missing occupancy summaries.\nExpected:\n  {luna_path}\n  {our_path}"
        )

    luna = load_occupancy_summary(luna_path)
    our = load_occupancy_summary(our_path)

    ln = occupancy_means(luna, "non-epilepsy", k)
    le = occupancy_means(luna, "epilepsy", k)
    on = occupancy_means(our, "non-epilepsy", k)
    oe = occupancy_means(our, "epilepsy", k)

    perm = hungarian_occupancy_informed(ln, le, on, oe)
    luna_d = delta_occupancy(le, ln)
    our_d = delta_occupancy(oe, on)[perm]
    r = concordance_r_delta(luna_d, our_d)

    print("=" * 60)
    print("Occupancy-informed cross-encoder concordance demo")
    print("=" * 60)
    print(f"k = {k}")
    print(f"Hungarian permutation (OUR state matched to LUNA i): {perm.tolist()}")
    print()
    print("LUNA Delta o (Epi - NonEpi), %:")
    print(" ", np.round(100 * luna_d, 2))
    print("OUR  Delta o aligned, %:")
    print(" ", np.round(100 * our_d, 2))
    print()
    print(f"r_Delta = {r:.4f}")
    if k == 4:
        print("(Paper primary result is approximately r_Delta = 0.96)")
    print()
    print("Note: frozen model weights are NOT required for this demo.")
    print("Place LUNA / OUR checkpoints under models/luna and models/our later.")


if __name__ == "__main__":
    main()
