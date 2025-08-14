# Xenium Raw Data Analysis Workflow

**Dataset:** *Xenium Human Lung Preview — Non-diseased FFPE*  
**Source & Download:** [10x Genomics — Xenium Human Lung Preview (standard)](https://www.10xgenomics.com/datasets/xenium-human-lung-preview-data-1-standard) — Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## Overview  
This repository, named **Xenium Raw Data Analysis Workflow**, implements a transparent and flexible pipeline for processing Xenium spatial transcriptomics data from raw output to spatial visualization. Unlike workflows that depend on Zarr or aggregated formats, this approach uses step-by-step raw data processing for reproducibility and educational clarity.

---

## Why this detailed pipeline matters

1. **Reproducibility & clarity**  
   You manually stream and filter transcripts (e.g., Q ≥ 20) and build the cell×gene matrix, making every step clear and auditable.

2. **Robustness to changes**  
   Xenium data format may change over time; this pipeline handles schema differences gracefully (e.g. variations in column names like `x_location` vs `x_centroid`).  
   :contentReference[oaicite:13]{index=13}

3. **Scalability & memory efficiency**  
   The two-pass Arrow/Parquet batching avoids memory issues, allowing for large datasets to be handled smoothly.

4. **Educational clarity**  
   Every transformation—loading raw data, QC, spatial embedding, clustering, and neighborhood analysis—is transparent and easy to follow.

5. **Customizable & extensible**  
   Users can easily adjust quality thresholds or extend the pipeline to other spatial platforms (e.g., CosMx, MERFISH).

---

## Repository Contents

- **scripts/unpack_all.py** — Extracts Xenium data from zipped output bundles.  
- **notebooks/03_preview_quickstart.ipynb** — Walk-through notebook to:
  - Load raw `cells.parquet` and `transcripts.parquet`, plus image and metrics files  
  - Filter and build a sparse count matrix  
  - Construct and QC an `AnnData` object  
  - Normalize, cluster, and visualize spatial patterns  
  - Compute neighborhood enrichment and save results

---

## Getting Started

1. Clone this repository (e.g., `git clone https://github.com/you/xenium-raw-data-analysis-workflow.git`).  
2. Download the Xenium dataset ZIP from the link above and place it in `data/`.  
3. Run `python scripts/unpack_all.py` to extract the dataset.  
4. Install dependencies (`scanpy`, `squidpy`, `spatialdata-io`, `pyarrow`, etc.).  
5. Execute the notebook to proceed from raw data to processed results.  
6. Explore outputs in `results/figures/` and the processed `.h5ad` file.

---

## Attribution  
Dataset: Xenium Human Lung Preview, 10x Genomics (CC BY 4.0) — cite per 10x Genomics guidelines.

---

**Repo Summary:**  
- Name: `xenium-raw-data-analysis-workflow` (clear, descriptive, follows naming best practices)  
- Purpose: Detailed, manual parsing and processing of Xenium raw data  
- Strengths: Transparency, flexibility, reproducibility over convenience.

Let me know if you’d like help renaming the GitHub repo or updating the header to reflect it in your notebooks/documentation!
::contentReference[oaicite:14]{index=14}

