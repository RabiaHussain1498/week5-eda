# Week 5 — Orders EDA

## What's here
A full EDA pipeline run end-to-end on a synthetic orders dataset,
deliberately generated with realistic data-quality problems: missing
values, inconsistent category labels, invalid quantities, price errors,
and duplicate records.

**Diagnosis** — `.info()`, `.describe()`, `.isna().sum()`, `.value_counts()`,
and extended validation checks (dtype drift, key-uniqueness, casing) to
surface every planted issue plus a couple that weren't explicitly named.
**Cleaning** — a per-column, justified fix for each issue (drop vs. fill vs.
targeted correction), not a blanket strategy.
**Visualization** — four charts (histogram, bar chart, scatter, boxplot),
each matched deliberately to the question it answers, built through
`fig, ax = plt.subplots()`.
**Findings** — three findings, each backed by a specific chart or number.

## Files
- `orders_eda.ipynb` — the full notebook, diagnosis through findings
- `summary.md` — summary of the dataset, fixes, findings, and
  an honest limitation, understanable without opening the notebook
- `gen_dataset.py` — generates the raw dataset from the required specifications
- `data/orders_raw.csv` — the uncleaned dataset as generated

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

## Notes
Notebook is confirmed clean on Restart Kernel and Run All before every commit.