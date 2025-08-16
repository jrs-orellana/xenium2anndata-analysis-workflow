#!/bin/bash
set -euo pipefail

DATA_DIR="data"
RAW_DIR="$DATA_DIR/raw"
OUT_DIR="$DATA_DIR/unpacked"

mkdir -p "$OUT_DIR"

# 1) Unpack the main *_outs.zip
for zip in "$RAW_DIR"/*_outs.zip; do
  folder="$(basename "$zip" .zip | tr '[:upper:]' '[:lower:]' | sed 's/_outs$//')"
  unzip -q -o "$zip" -d "$OUT_DIR/$folder"
done

# 2) Extract cell_feature_matrix.tar.gz if present
find "$OUT_DIR" -type f -name "cell_feature_matrix.tar.gz" | while read -r tarfile; do
  target_dir="$(dirname "$tarfile")/cell_feature_matrix"
  mkdir -p "$target_dir"
  echo "[INFO] Extracting: $tarfile → $target_dir"
  tar -xzf "$tarfile" -C "$target_dir"
done

# 3) Decompress features.tsv.gz but keep original
find "$OUT_DIR" -type f -path "*/cell_feature_matrix/features.tsv.gz" | while read -r gzfile; do
  echo "[INFO] Decompressing: $gzfile"
  gunzip -k -f "$gzfile"
done

echo "[DONE] All files unpacked and features.tsv available."
