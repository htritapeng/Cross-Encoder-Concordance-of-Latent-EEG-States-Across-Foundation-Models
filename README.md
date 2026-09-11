# Cross-Encoder Concordance of Latent EEG States Across Foundation Models

**Paper:** ISDS 2026 (Springer CCIS), Paper ID 4217  
**Authors:** Rita Huan-Ting Peng, Nhat Bui, Chun-Yi Lin

This repository contains a **minimal, reproducible package** for the paper’s primary concordance analysis:

1. Load group-mean latent-state occupancy for **LUNA-Base** and **OUR** (lightweight model)  
2. Align states with the **Hungarian** algorithm (occupancy-informed)  
3. Compute epilepsy-related occupancy change \(\Delta o = o_{\mathrm{Epi}} - o_{\mathrm{NonEpi}}\)  
4. Report cross-encoder concordance \(r_\Delta\)

> **Frozen model weights are optional for the demo.**  
> Placeholders are ready under `models/luna` and `models/our` for you to upload later.

---

## Package structure

```text
.
├── README.md                
├── requirements.txt
├── .gitignore
├── code/                     ← analysis utilities
│   └── alignment.py          ← Hungarian matching + r_Delta helpers
├── demo/                     ← runnable examples
│   └── run_occupancy_concordance_demo.py
├── models/                   ← FROZEN WEIGHTS (upload later)
│   ├── luna/                 ← put LUNA-Base checkpoint here
│   └── our/                  ← put OUR lightweight checkpoint here
├── data/
│   ├── README.md             ← input data format details
│   └── input/
│       ├── occupancy/        ← demo-ready occupancy exports (included)
│       │   ├── luna/
│       │   └── our/
│       ├── embeddings/       ← optional window embeddings (empty for now)
│       │   ├── luna/
│       │   └── our/
│       └── labels/           ← optional subject labels (empty for now)
└── outputs/                  ← generated outputs (gitignored)
```

---

## What you need

| Item | Required for demo? | Where |
|------|--------------------|--------|
| Occupancy summaries (`k=3,4,5`) | **Yes** (included) | `data/input/occupancy/` |
| Frozen LUNA weights | No (later) | `models/luna/` |
| Frozen OUR weights | No (later) | `models/our/` |
| Raw TUEP EEG | No (not redistributed) | Obtain from TUH / TUEP |
| Window embeddings | No (for advanced analyses) | `data/input/embeddings/` |

---

## Input data structure (short)

### Occupancy (included)

```text
data/input/occupancy/luna/occupancy_summary_k4.json
data/input/occupancy/our/occupancy_summary_k4.json
```

Each summary JSON has group means for `non-epilepsy` and `epilepsy`:

- `occupancy_state_0_mean` … `occupancy_state_{k-1}_mean`

Subject-level CSVs (`occupancy_k{K}.csv`) include `subject_id`, `group` (`0`/`1`), and per-state occupancy.

See `data/README.md` for full details.

### Frozen models (you upload later)

```text
models/luna/   # e.g. luna_base.pt
models/our/    # e.g. our_lightweight.pt
```

---

## Setup

```bash
# from this repository root
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS / Linux
# source .venv/bin/activate

pip install -r requirements.txt
```

---

## Run the demo

From the **repository root**:

```bash
# primary paper setting (k=4) → expect r_Delta ≈ 0.96
python demo/run_occupancy_concordance_demo.py

# sensitivity
python demo/run_occupancy_concordance_demo.py --k 5
python demo/run_occupancy_concordance_demo.py --k 3
```

### Expected output (k=4)

- Hungarian permutation matching OUR states to LUNA  
- \(\Delta o\) vectors for both encoders  
- \(r_\Delta \approx 0.96\)

---

## Study pipeline (high level)

```text
TUEP EEG
   │
   ├─► frozen LUNA encoder ─► k-means states ─► occupancy
   │                                              │
   └─► frozen OUR  encoder ─► k-means states ─► occupancy
                                                  │
                                    Hungarian alignment
                                                  │
                                         Δo and r_Delta
```

The included demo starts from **precomputed occupancy** (right side of the pipeline).  
Encoding from raw EEG with frozen weights can be added after you upload models.

---

## Citation

```bibtex
@inproceedings{peng2026crossencoder,
  title={Cross-Encoder Concordance of Latent EEG States Across Foundation Models},
  author={Peng, Rita Huan-Ting and Bui, Nhat and Lin, Chun-Yi},
  booktitle={International Symposium on Intelligent Systems and Data Science (ISDS)},
  series={Communications in Computer and Information Science},
  publisher={Springer},
  year={2026},
  note={Paper ID 4217}
}
```

---

## License / data note

- Code in this repo: see repository license (or add `LICENSE` before publishing).  
- **TUEP/TUEG raw EEG is not included.** Follow the Temple University Hospital EEG data use agreements.  
- Do not commit large `.pt` / `.npy` files unless you intend to distribute them.
