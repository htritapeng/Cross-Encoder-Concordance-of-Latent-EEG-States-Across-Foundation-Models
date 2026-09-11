# Input data layout

## What is included (demo-ready)

Precomputed **subject-level occupancy** used by the paper's primary concordance analysis:

```text
data/input/occupancy/
  luna/
    occupancy_summary_k3.json
    occupancy_summary_k4.json
    occupancy_summary_k5.json
    occupancy_k3.csv
    occupancy_k4.csv
    occupancy_k5.csv
  our/
    occupancy_summary_k3.json
    occupancy_summary_k4.json
    occupancy_summary_k5.json
    occupancy_k3.csv
    occupancy_k4.csv
    occupancy_k5.csv
```

### Occupancy summary JSON (group means)

Each `occupancy_summary_k{K}.json` contains:

```json
{
  "non-epilepsy": {
    "n_rows": "...",
    "occupancy_state_0_mean": "...",
    "occupancy_state_0_std": "...",
    "...": "..."
  },
  "epilepsy": { "...": "..." },
  "pairwise_mannwhitney_occupancy": { "...": "..." }
}
```

Groups:
- `non-epilepsy`
- `epilepsy`

### Occupancy CSV (subject level)

Each `occupancy_k{K}.csv` has columns like:

| column | meaning |
|--------|---------|
| `subject_id` | TUEP subject id |
| `group` | `0` = non-epilepsy, `1` = epilepsy |
| `k` | number of states |
| `occupancy_state_0` ... `occupancy_state_{k-1}` | subject occupancy |

Group labels are already in these CSVs (no separate `labels/` folder).

### Raw TUEP EEG

Raw EEG is **not** redistributed here (TUEP / TUH license). Obtain TUEP from the
Temple University Hospital EEG resources and preprocess as described in the paper
(band-pass 0.3–75 Hz, notch 60 Hz, 19-channel 10–20, 200 Hz, 30 s windows).
