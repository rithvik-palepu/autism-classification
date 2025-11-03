import numpy as np
from pathlib import Path

def vectorize_connectomes(matrix):
    triu_idx = np.triu_indices_from(matrix, 1)
    return matrix[triu_idx]

connectome_dir = Path("data/interim/connectomes_cc200")
files = sorted(connectome_dir.glob("*.npy"))

X = []
subjects = []

for f in files:
    mat = np.load(f)
    vec = vectorize_connectomes(mat)
    X.append(vec)
    subjects.append(f.stem.split("_rois")[0])

X = np.array(X)
print(X.shape)