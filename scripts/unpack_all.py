#!/usr/bin/env python3
"""
unpack_all.py
-------------
Unpack Xenium Output Bundle zip files into structured folders.

Usage:
    python scripts/unpack_all.py

Expected layout before running:
    data/
      Xenium_Preview_Human_Non_diseased_Lung_With_Add_on_FFPE_outs.zip
"""

import pathlib
import zipfile
import hashlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

def sha256sum(path):
    """Return SHA256 checksum of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def unpack_zip(zip_path, out_dir):
    """Unpack a Xenium Output Bundle zip into out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(out_dir)
    print(f"[OK] Unpacked to: {out_dir}")

def main():
    zips = sorted(DATA_DIR.glob("*_outs.zip"))
    if not zips:
        print("[WARN] No *_outs.zip files found in data/")
        return

    for zip_path in zips:
        folder_name = zip_path.stem.replace("_outs", "").lower()
        out_dir = DATA_DIR / folder_name
        print(f"[INFO] Processing: {zip_path.name}")
        print(f"       SHA256: {sha256sum(zip_path)}")
        unpack_zip(zip_path, out_dir)

    print("\n[ALL DONE] You can now load the unpacked folders into your notebook.")

if __name__ == "__main__":
    main()
