# Data notes

## `occupancy/`
Subject-level occupancy CSVs and group-mean summary JSONs for LUNA and OUR (USE-FM/USFEEG)
at \(k=3,4,5\). Group `0` = non-epilepsy, `1` = epilepsy (as in the original exports).

## `metrics/`
Global WCSS and Davies–Bouldin index vs \(k=3\ldots20\) from the LatentBenchmark TUEP run
(`luna_*`, `usfeeg_*`).

## `results/`
Precomputed camera-ready numeric summaries (including PCA co-assignment \(r_\Delta\)).

## Not packaged
- Raw TUEP EEG
- Full mLTD per-subject JSON trees
- PCA window latents (`.npy`) required to **re-run** co-assignment from scratch

Point external PCA latents (if re-running) to your local LatentBenchmark folder, e.g.:

`...\IEEE_ SPMB\LatentBenchmark\TUEP\global_run4\pca_latents\{luna,usfeeg}\`
