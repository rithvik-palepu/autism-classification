import sys

import numpy as np
from pathlib import Path
import os

def compute_connectome(ts):
    # Compute correlation matrix (Fisher-z transformed)
    corr = np.corrcoef(ts, rowvar=False)
    # Fisher z-transform for normalization
    corr = np.arctanh(np.clip(corr, -0.999999, 0.999999))
    return corr

def process_all(input_dir, output_dir):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    files = list(input_dir.glob("*.1D"))
    print(f"Found {len(files)} files.")

    for f in files:
        ts = np.loadtxt(f)
        conn = compute_connectome(ts)
        out_path = output_dir / (f.stem + ".npy")
        np.save(out_path, conn)
        print(f"Saved {out_path.name}")

if __name__ == "__main__":
    input_dir = "/Users/rithvikpalepu/PycharmProjects/autism-classification/data/raw/abide_cc200/rois_cc200"
    output_dir = "data/interim/connectomes_cc200"
    process_all(input_dir, output_dir)