# autism-classification
Using ABIDE datasets to process sMRI and fMRI images and classify Autism using machine learning pipelines.

## Project Structure
data/
├── raw/ # downloaded ABIDE files
├── interim/ # cleaned / merged phenotypic and feature data
└── processed/ # features ready for ML
notebooks/
├── 01_explore.ipynb # EDA, visualization, phenotypic QC
├── 02_features.ipynb # feature extraction & preprocessing
├── 03_models.ipynb # model training & cross-validation
└── 04_interpret.ipynb # feature importance & visualization

src/
├── io.py # data loading utilities
├── features.py # feature engineering helpers
├── models.py # ML pipeline, training, evaluation
└── utils.py # random seeds, logging, metrics

reports/
└── figures/ # exported plots & result summaries

## Getting Started
1) Clone this repo
   - git clone https://github.com/rithvik-palepu/autism-classification.git
   - cd autism-classification
     
2) Install Dependencies
   - pip install -r "requirements.txt"

3) Download ABIDE Data
   - Visit http://preprocessed-connectomes-project.org/abide/
   - Choose a pre-processing pipeline
   - place .mat or .csv connectivity files into data/raw/

4) Run Jupyter Notebooks in order
   - 01_explore.ipynb → data inspection
   - 02_features.ipynb → feature creation
   - 03_models.ipynb → ML training
   - 04_interpret.ipynb → analysis & figures

## Repro
  - Python 3.10+
  - Random seed: 42
  - All transformations (scaling, PCA, feature selection) occur inside CV folds to avoid data leakage.
  - Metrics reported: Accuracy, ROC-AUC, and site-wise generalization.

## MIT License
Copyright (c) [2025] [Rithvik Palepu]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
