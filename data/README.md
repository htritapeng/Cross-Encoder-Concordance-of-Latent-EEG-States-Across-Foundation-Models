# Input data layout

## What is included now (demo-ready)

Precomputed **subject-level occupancy** summaries used by the paper's primary concordance analysis:

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
    "n_rows": ...,
    "occupancy_state_0_mean": ...,
    "occupancy_state_0_std": ...,
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

---

## Placeholders for full pipeline (upload later)

```text
data/input/embeddings/
  luna/     # optional: segment/window embeddings (.npy), one file per subject
  our/      # optional: segment/window embeddings (.npy), one file per subject

data/input/labels/
  subject_groups.csv   # optional: subject_id, group
```

### Suggested embedding file naming

```text
data/input/embeddings/luna/<subject_id>.npy   # shape (n_windows, dim)
data/input/embeddings/our/<subject_id>.npy    # shape (n_windows, dim)
```

Same `subject_id` and aligned window order are required for label-independent
co-assignment analysis.

### Raw TUEP EEG

Raw EEG is **not** redistributed here (TUEP / TUH license). Obtain TUEP from the
Temple University Hospital EEG resources and preprocess as described in the paper
(band-pass 0.3–75 Hz, notch 60 Hz, 19-channel 10–20, 200 Hz, 30 s windows).
