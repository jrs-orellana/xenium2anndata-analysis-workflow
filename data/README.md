# Data Directory

This folder contains the raw and unpacked Xenium dataset used for analysis.

## Structure

- **raw/**
  - `Xenium_Preview_Human_Non_diseased_Lung_With_Add_on_FFPE_outs.zip`  
    Original compressed dataset from Xenium preview.

- **unpacked/**
  - `xenium_preview_human_non_diseased_lung_with_add_on_ffpe/`  
    Unzipped dataset containing processed outputs, including spatial coordinates, transcript data, cell boundaries, and summary metrics.

## Notes
- The raw file should remain unchanged as the source reference.
- The unpacked folder is used directly by scripts and notebooks for analysis.
- Ensure the dataset is unzipped before running any processing scripts.
