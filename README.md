# Uni-FEP-Benchmarks

## Overview

**Uni-FEP-Benchmarks** is a benchmark dataset designed to systematically evaluate **Uni-FEP**, a free energy perturbation (FEP) method for accurate and efficient binding free energy calculations. This repository provides computational results across diverse protein-ligand systems and complex chemical transformations, facilitating validation and optimization of the Uni-FEP methodology.

## Objectives

By compiling well-structured benchmark cases, this repository aims to:

1. **Improve the stability of Uni-FEP**  
   - Through extensive testing across various systems, we aim to identify potential weaknesses in Uni-FEP and refine its robustness.

2. **Establish standardized test data for tracking performance changes**  
   - By maintaining a structured benchmark dataset, we can systematically analyze the impact of each Uni-FEP update on computational accuracy.

3. **Reduce the cost of FEP adoption for users**  
   - This repository is designed as a long-term project. Over time, as more benchmark cases are added, users may directly request pre-constructed systems from this dataset, allowing them to focus solely on predicting new compounds without having to reconstruct the entire system.

## Repository Structure

Each system is organized into a separate folder, containing:

```
scripts/
└── gen_figure.py       # Script for generating dG comparison plots based on result_dG.csv

uni_fep_benchmarks/
│── system_1/  
│   ├── README.md        # Brief description of the system  
│   ├── result_dG.png    # Visualization of FEP-calculated dG  
│   ├── result_dG.csv    # Numerical results of dG comparisons  
│  
│── system_2/  
│   ├── README.md  
│   ├── result_dG.png  
│   ├── result_dG.csv  
│  
└── ...
```

## File Descriptions

- **`README.md`**: Contains a brief summary of the system, including error statistics (e.g., RMSE of dG and ddG).
- **`result_dG.png`**: Graphical representation of **FEP-derived binding free energies (dG)** compared to experimental values.
- **`result_dG.csv`**: A table containing RBFE-predicted binding free energies (`fep_dG`) and experimental measurements (`exp_dG`).

#### `result_dG.csv` Example (RBFE-calculated dG values)
| ligand_smiles | ligand_name | exp_dG (kcal/mol) | fep_dG (kcal/mol) | fep_dG_std (kcal/mol) |
|----------------|--------------|-----------------|-----------------|-----------------|
| 'Ligand_SMILES' | 'Ligand_Name' | -7.5 | -7.2 | 0.15 |
| 'Ligand_SMILES' | 'Ligand_Name' | -8.1 | -7.9 | 0.08 |

## Data Update Guidelines

When submitting new benchmark data via a **Merge Request**, please include the following information at least to ensure transparency and reproducibility:

1. **Uni-FEP version** used for this dataset  
2. **Simulation parameters** (e.g., lambda windows, simulation time, force field)  

This metadata should be included in the **Merge Request description**.

By following these guidelines, we ensure consistency across datasets and allow for fair comparisons between different versions of Uni-FEP.

