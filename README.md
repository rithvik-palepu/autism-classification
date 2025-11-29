Multisite Autism Classification Using Functional Connectomes (ABIDE I): A Reproducible LOSO Benchmark
A complete end-to-end functional-connectivity ML pipeline with harmonization, EDA, and strict cross-site evaluation.

Abstract
Machine-learning prediction of autism spectrum disorder (ASD) using resting-state functional MRI is an active research area, but multisite variability severely limits model generalization.
In this project, we develop a fully reproducible baseline pipeline for ASD classification using the ABIDE I dataset.
We extract functional connectomes (CC200 parcellation), perform exploratory data analysis, visualize site effects via PCA, apply ComBat harmonization, and evaluate classification performance using Leave-One-Site-Out (LOSO) cross-validation — the strictest test of multisite generalization.
A logistic regression classifier achieved:
Mean LOSO AUC: ~0.70
Mean LOSO Accuracy: ~0.65
These results are consistent with prior ABIDE literature and illustrate (1) strong site-induced batch effects, (2) partial but incomplete site correction using ComBat, and (3) the difficulty of ASD-vs-TD classification in real multisite settings.
This repository provides a clear, transparent baseline for future work using GNNs, domain adaptation, or more advanced harmonization approaches.

1. Introduction
Neuroimaging-based ASD classification is challenging due to:
high inter-site variability (scanner, TR, motion, protocols),
small sample sizes per site,
subtle neural signatures of ASD.
The ABIDE I dataset is widely studied but notoriously heterogeneous.
Many published results depend heavily on site selection or evaluation procedures.
This project aims to:
Build a clean, reproducible baseline for multisite ASD classification.
Use functional connectomes as features.
Apply site harmonization (ComBat).
Use LOSO (leave-one-site-out) evaluation to test generalization.
This README follows a research-paper structure for clarity and professionalism.

2. Dataset
ABIDE I
1112 subjects originally
Resting-state fMRI from 17 international sites
Phenotypic data (age, sex, diagnosis) included
Diagnosis: ASD vs TD (Typically Developing)
Parcellation
Craddock CC200
200 ROIs
~19,900 unique ROI-to-ROI edges per connectome
Final cleaned dataset
After removing subjects with missing values:
848 subjects
200×200 connectivity matrices
Flattened into 19,900 features

3. Methods
3.1 Connectome Extraction
We compute functional connectivity following prior ABIDE pipelines [4,6]:
Load C-PAC preprocessed ROI time series
Compute Pearson correlation
Apply Fisher z-transform
Vectorize upper triangle

3.2 Data Cleaning
Remove participants with any missing values
Align connectivity matrices with diagnosis and site labels

3.3 Site Harmonization with ComBat
Multisite fMRI shows site-specific mean and variance shifts [3,4].
We use neuroCombat (Fortin et al., 2018) [3] to adjust for:
Batch (site) effects
While preserving biological covariates (diagnosis)

3.4 Dimensionality Reduction (PCA)
Following Nielsen et al. (2013) [4], we use PCA for visualization:
Pre-ComBat: strong site clustering
Post-ComBat: reduced site structure, but not eliminated
ASD/TD classes remain difficult to separate → consistent with prior work [4–7]

3.5 Classification Model
A simple logistic regression classifier (L2 regularization) is used as a transparent baseline, following prior connectome studies [4,5].

3.6 Evaluation (Leave-One-Site-Out)
LOSO is recommended for fair multisite evaluation [4,7]:
Train on all sites except one
Test on the held-out site
Compute AUC and accuracy
Repeat for all sites
This tests true out-of-distribution performance.

4. Results
4.1 PCA Visualization
Consistent with [4,5], PCA reveals:
Large site-driven variance pre-harmonization
<img width="567" height="463" alt="image" src="https://github.com/user-attachments/assets/fc015a40-0482-4fa1-8ed8-7cbb4e63df6f" />

Reduced but non-zero site effects after ComBat
<img width="545" height="419" alt="image" src="https://github.com/user-attachments/assets/359f4a33-202c-47c8-8585-859ec3c3eb99" />

Diagnosis separation remains weak, consistent with ABIDE literature
<img width="431" height="350" alt="image" src="https://github.com/user-attachments/assets/e9fe369a-f8c1-4e56-8725-9eb31a446c28" />


4.2 LOSO Classification Performance
Below is an example of site-wise results:
Site	AUC	Accuracy
YALE	0.848	0.745
USM	0.816	0.738
NYU	0.774	0.686
PITT	0.733	0.705
MAX	0.595	0.619
STANFORD	0.480	0.472
Mean	~0.70	~0.65
<img width="266" height="359" alt="image" src="https://github.com/user-attachments/assets/60def120-5d4c-4c4b-877a-77499aab5adf" />

4.3 Interpretation
Performance aligns with ABIDE multisite studies (AUC 0.65–0.72) [4–7]
Some sites generalize well (e.g., YALE, USM)
Others exhibit scanner/population mismatch (e.g., STANFORD)
Site effects remain the primary challenge in ABIDE classification
These findings match the consensus in the literature: ASD classification from resting-state FC is difficult, and multisite evaluation is crucial [4]

5. Discussion
Key conclusions:
Site-specific variance dominates functional connectivity patterns
ComBat reduces but does not eliminate inter-site differences [3]
Logistic regression is a strong, interpretable baseline [4]
GNNs [9], domain-adaptation methods [7], and multi-parcellation fusion can improve performance
This repository provides a fully reproducible benchmark for future methods

6. Repository Structure
/
├── data/
│   ├── raw/                 # Downloaded ABIDE ROIs
│   ├── interim/             # Connectomes per subject
│   └── processed/           # ComBat harmonized data
│
├── notebooks/
│   ├── 01_explore.ipynb     # EDA, PCA, distribution checks
│   ├── 02_features.ipynb    # Connectome vectorization
│   └── 03_models.ipynb      # ComBat, LOSO, classification
│
├── src/
│   └── ...                  # Utility modules (optional)
│
└── README.md                # This file
7. Usage
Clone & setup
git clone https://github.com/rithvik-palepu/autism-classification
cd autism-classification
pip install -r requirements.txt
Run notebooks in order
01_explore.ipynb
02_features.ipynb
03_models.ipynb

8. References
[1] Di Martino, A., et al. (2014). The autism brain imaging data exchange: Towards a large-scale evaluation of the intrinsic brain architecture in autism. Mol Psychiatry.
[2] Craddock, R. C., et al. (2012). A whole brain fMRI atlas generated via spatially constrained spectral clustering. Hum Brain Mapp.
[3] Fortin, J.-P., et al. (2018). Harmonization of multi-site diffusion tensor imaging data. NeuroImage. (Introduces NeuroCombat; applied widely to rs-fMRI).
[4] Nielsen, J. A., et al. (2013). Multisite functional connectivity MRI classification of autism: ABIDE results. Frontiers in Human Neuroscience.
[5] Abraham, A., et al. (2017). Deriving reproducible biomarkers from multi-site resting-state data: an autism-based example. NeuroImage.
[6] Heinsfeld, A. S., et al. (2018). Identification of autism spectrum disorder using deep learning on fMRI data. J Neuroimaging.
[7] Yan, K., et al. (2019). Domain adaptation for neuroimaging classifiers. Human Brain Mapping.
[8] Eslami, T., et al. (2021). * ASD classification using deep CNN models on ABIDE.* (Single-site results can exceed 90% accuracy).
[9] Ktena, S. I., et al. (2018). Metric learning with spectral graph convolutions for brain connectomes. MICCAI.
9. Acknowledgements
Thanks to:
The ABIDE consortium
C-PAC preprocessing team
The developers of NeuroCombat, NumPy, Pandas, and Scikit-Learn

