# README for Running "Tennis Analytics Using Process Analysis Toolkit (PAT) on Ranking Model"

## Introduction
This README guides you through the process of running the "Tennis Analytics Using Process Analysis Toolkit (PAT) on Ranking Model" Jupyter Notebook. This notebook focuses on analyzing tennis data and applying a ranking model using PAT.

## Prerequisites
Before running the notebook, ensure you have the following:
- Python 3 (latest version)
- Jupyter Notebook or JupyterLab
- The `tennis_examples.zip` file's contents extracted into this folder, available in the provided Google Drive link
(We have them already in here, this is just in case a test from scratch is desired)
- `tennisabstract-v2-combined.csv` file, placed in the root directory of the `tennis_examples` folder

## Installation
1. **Install Python**: Download and install the latest version of Python 3 from [python.org](https://www.python.org/).
2. **Install Jupyter**: Run `pip install notebook` to install Jupyter Notebook.
3. **Download Required Files**: Download `tennis_examples.zip` from the provided Google Drive link and extract it to your desired location. Ensure that the `tennisabstract-v2-combined.csv` file is inside the root directory of the `tennis_examples` folder.

## Running the Notebook
Simply run Jupyter Notebook or JupyterLab, navigate to the notebook `Ranking Pipeline.ipynb`, and open it. Run the notebook cells sequentially by pressing `Shift + Enter` on each cell.

## Outputs
The notebook will generate several key files:
- `MatchedRecords.csv` for the matches determined to be analysed.
- `helper.csv`: For intermediate data processing.
- Files for PAT model simulation in the `pcsp` folder.
- `rank.csv` and `base.csv`: For betting simulation.

## Additional Notes
- No additional Python packages are required to run the notebook.
- Follow any specific instructions within the notebook for details on running each cell.
- The pcsp.zip file should be the pcsp folder generated by `Ranking Pipeline.ipynb`. 
