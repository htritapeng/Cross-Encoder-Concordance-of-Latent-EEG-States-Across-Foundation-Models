# Updated results: WCSS / elbow + \(r_\Delta\) across \(k\)

**Generated:** from existing LatentBenchmark WCSS/DBI CSVs + ISDS occupancy summaries  
**Saved also as:** `WCSS_and_rDelta_across_k_results.txt`

---

## Short answer

**Partially yes.**

| Item | Available now? | Result |
|------|----------------|--------|
| WCSS for LUNA & USE-FM, \(k=3\ldots20\) | **Yes** | Ready to plot elbow |
| DBI for both, \(k=3\ldots20\) | **Yes** | Soft / not a sharp elbow at 4 |
| \(r_\Delta\) across several \(k\) | **Only \(k=3,4,5\)** | Occupancy-informed high at 3–4, drops at 5 |
| Independent NonEpi-only \(r_\Delta\) | Computed for 3–4–5 | **Collapses at \(k=3,4\)** (negative); moderate at \(k=5\) |

You do **not** yet have occupancy summaries for \(k=6,\ldots,20\), so full concordance-vs-\(k\) curves beyond 5 need new clustering/occupancy exports.

---

## 1. WCSS elbow (both encoders)

Largest relative WCSS drop:

- **USE-FM:** \(k=3\to4\) = **−19.4%** (biggest step), then ~9%, 8%, …
- **LUNA:** \(k=3\to4\) = **−10.7%**, then ~9%, 8%, …

After \(k\approx8\), drops are small (~2–4%). So \(k=4\) is a **plausible early elbow**, especially for USE-FM, but not a dramatic unique kink for LUNA.

**DBI (lower better):** at \(k=4\), DBI is **worse** than at \(k=3\) for both (LUNA 1.56 vs 1.37; USE-FM 1.16 vs 1.11). So do **not** claim DBI selects \(k=4\); justify with WCSS diminishing returns + primary analysis convention.

---

## 2. \(r_\Delta\) sensitivity (available \(k=3,4,5\) only)

| \(k\) | Occupancy-informed \(r_\Delta\) | NonEpi-only independent \(r_\Delta\) | # permutations |
|------|----------------------------------|--------------------------------------|----------------|
| 3 | **+0.99** | **−0.56** | 6 |
| 4 | **+0.96** | **−0.25** | 24 |
| 5 | **+0.58** | **+0.47** | 120 |

### What this means for the paper

1. **Occupancy-informed concordance is not unique to \(k=4\)** — also very high at \(k=3\), but **drops to 0.58 at \(k=5\)**. So the “0.96 story” is strongest at small \(k\); report this transparently.
2. **Independent NonEpi-only alignment does not recover high \(r_\Delta\) at \(k=3\) or \(k=4\)** (negative). At \(k=5\) independent and occupancy-informed are closer (~0.47 vs 0.58).
3. This **supports the reviewers’ circularity concern** for the headline \(r_\Delta=0.96\): under an Epi-independent matching criterion, concordance at \(k=4\) does **not** stay high.
4. Camera-ready must either:
   - lead with honest independent-alignment results + demote 0.96 to occupancy-informed sensitivity, **or**
   - try a better independent criterion (e.g. **centroids**) before finalizing claims.

---

## 3. What you still need for a full “across \(k\)” story

To report concordance for \(k=6,7,\ldots\):

- Re-run / export `occupancy_summary_k{k}.json` for both encoders (same pipeline as k=3/4/5), **or**
- Recompute occupancy from existing state assignments if those files exist elsewhere.

Until then, report:

- WCSS/DBI for \(k=3\ldots20\) (full),
- \(r_\Delta\) sensitivity for **\(k=3,4,5\)** only (honest about the limit).

---

## 4. Suggested camera-ready wording (honest)

> WCSS for both encoders decreases sharply from \(k=3\) to \(k=4\) (especially USE-FM, −19.4%) and then more gradually; we therefore emphasize \(k=4\) as a primary exploratory operating point, not a uniquely optimal clinical partition. Occupancy-informed \(\Delta\)-occupancy concordance is high at \(k=3\) and \(k=4\) (\(r_\Delta=0.99\) and \(0.96\)) but declines at \(k=5\) (\(r_\Delta=0.58\)). Under NonEpi-only (label-light) alignment, \(r_\Delta\) is not high at \(k=4\), indicating that the occupancy-informed value should be interpreted as concordance after occupancy-informed matching rather than as an independent validation.

---

## Files

- Raw numbers: `revision/WCSS_and_rDelta_across_k_results.txt`
- Script: `revision/compute_wcss_rdelta_sensitivity.py`
