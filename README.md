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

## Summary of Benchmark Results
| System | N_Ligands | RMSE (kcal/mol) | R² | Kendall's tau |
|---|---|---|---|---|
| 3CLPro_hist | 5 | 0.83 | 0.69 | 0.80 |
| A2A-Deflorian_GPCRFEP | 10 | 0.76 | 0.83 | 0.69 |
| A2A-Lenselink_GPCRFEP | 7 | 0.54 | 0.84 | 0.62 |
| A2A-Minetti_GPCRFEP | 9 | 0.91 | 0.50 | 0.39 |
| A2A-Piersanti_GPCRFEP | 7 | 0.38 | 0.33 | 0.62 |
| ACK1_hist | 6 | 1.10 | 0.71 | 0.60 |
| AKR1C3_CHEMBL4428988 | 11 | 0.90 | 0.59 | 0.67 |
| AMPD2_CHEMBL5240593 | 14 | 1.36 | 0.54 | 0.46 |
| AURKA_CHEMBL2382841 | 7 | 1.12 | 0.79 | 0.59 |
| BACE1_CHEMBL2352381 | 10 | 0.96 | 0.89 | 0.91 |
| BCL6_hist | 6 | 1.01 | 0.84 | 0.60 |
| BRD4_CHEMBL2183681 | 12 | 0.48 | 0.77 | 0.34 |
| BRPF1_CHEMBL3385101 | 17 | 0.65 | 0.60 | 0.62 |
| CDK2_CHEMBL2013356 | 12 | 1.21 | 0.37 | 0.21 |
| CDK4_hist | 6 | 0.38 | 0.84 | 0.87 |
| CMA1_CHEMBL4182330 | 9 | 0.90 | 0.67 | 0.50 |
| CREBBP_CHEMBL3817157 | 12 | 0.56 | 0.91 | 0.82 |
| CSNK1D_CHEMBL2211470 | 13 | 1.48 | 0.47 | 0.50 |
| CXCR4_GPCRFEP | 9 | 1.11 | 0.44 | 0.25 |
| D3_GPCRFEP | 6 | 1.09 | 0.67 | 0.87 |
| DOR_GPCRFEP | 11 | 0.83 | 0.59 | 0.60 |
| DOT1L_CHEMBL4480297 | 8 | 2.29 | 0.90 | 0.79 |
| DPP4_CHEMBL951312 | 23 | 0.74 | 0.61 | 0.50 |
| DUT_CHEMBL2060493 | 13 | 1.10 | 0.40 | 0.49 |
| EIF2AK3_CHEMBL2444392 | 12 | 1.17 | 0.65 | 0.60 |
| Eg5_hist | 7 | 0.40 | 0.58 | 0.52 |
| F10_CHEMBL661585 | 14 | 1.13 | 0.63 | 0.67 |
| F10_CHEMBL661586 | 13 | 0.85 | 0.41 | 0.51 |
| F2_CHEMBL1067528 | 16 | 0.84 | 0.65 | 0.58 |
| FKBP12_hist | 6 | 0.53 | 0.84 | 0.87 |
| FKBP1A_CHEMBL678145 | 10 | 0.70 | 0.66 | 0.42 |
| FXR_hist | 6 | 0.69 | 0.69 | 0.60 |
| GAK_CHEMBL4736826 | 21 | 1.11 | 0.63 | 0.56 |
| GCKR_CHEMBL3751185 | 11 | 0.69 | 0.87 | 0.67 |
| GCKR_CHEMBL3751192 | 11 | 0.74 | 0.87 | 0.67 |
| Galectin-3_hist | 8 | 0.90 | 0.89 | 0.93 |
| HNE_hist | 6 | 1.28 | 0.96 | 0.73 |
| HSP90AA1_CHEMBL3427922 | 9 | 0.99 | 0.62 | 0.67 |
| HSP90_hist | 11 | 1.29 | 0.71 | 0.73 |
| IGF1R_CHEMBL1045057 | 9 | 1.08 | 0.38 | 0.54 |
| JAK1_CHEMBL4620434 | 10 | 0.51 | 0.65 | 0.72 |
| JAK2_CHEMBL3625473 | 15 | 0.84 | 0.42 | 0.45 |
| JAK2_CHEMBL3627422 | 12 | 0.69 | 0.60 | 0.42 |
| JAK2_CHEMBL4150584 | 15 | 0.83 | 0.55 | 0.44 |
| KIF11_CHEMBL1037992 | 14 | 0.70 | 0.61 | 0.59 |
| KIF11_CHEMBL1694081 | 22 | 1.10 | 0.58 | 0.62 |
| KLK3_CHEMBL4844448 | 26 | 1.01 | 0.61 | 0.64 |
| KRAS-G12D_hist | 10 | 0.76 | 0.91 | 0.87 |
| LCK_CHEMBL903614 | 11 | 0.59 | 0.74 | 0.64 |
| MAOB_CHEMBL3588480 | 7 | 1.67 | 0.61 | 0.43 |
| MAP4K4_CHEMBL3755426 | 15 | 0.53 | 0.75 | 0.62 |
| MAPK14_CHEMBL1101788 | 8 | 0.65 | 0.66 | 0.50 |
| MAPK14_CHEMBL1787752 | 18 | 1.30 | 0.70 | 0.37 |
| MAPK14_CHEMBL2061259 | 11 | 1.47 | 0.45 | 0.70 |
| MELK_CHEMBL3824963 | 13 | 0.91 | 0.57 | 0.35 |
| MELK_CHEMBL4006633 | 8 | 0.79 | 0.72 | 0.62 |
| MET_CHEMBL2032485 | 8 | 1.05 | 0.90 | 0.79 |
| MMP13_CHEMBL1798873 | 13 | 1.22 | 0.83 | 0.58 |
| Menin_cyclic_peptide | 16 | 0.90 | 0.46 | 0.50 |
| NEK2_CHEMBL1693342 | 11 | 1.12 | 0.35 | 0.45 |
| NR1H2_CHEMBL907758 | 8 | 1.61 | 0.63 | 0.64 |
| OX2-set1_GPCRFEP | 27 | 0.88 | 0.57 | 0.57 |
| OX2-set2_GPCRFEP | 24 | 1.07 | 0.25 | 0.35 |
| PAK4_hist | 10 | 0.58 | 0.66 | 0.64 |
| PCSK9_cyclic_peptide | 18 | 0.77 | 0.51 | 0.47 |
| PDE1B_CHEMBL4011522 | 13 | 1.16 | 0.51 | 0.53 |
| PDE4B_CHEMBL3374901 | 13 | 0.62 | 0.79 | 0.68 |
| PDE4D_CHEMBL3374902 | 12 | 1.05 | 0.55 | 0.61 |
| PDE5A_CHEMBL968866 | 14 | 0.80 | 0.48 | 0.54 |
| PDK2_CHEMBL5057865 | 20 | 0.45 | 0.88 | 0.82 |
| PDPK1_CHEMBL1942054 | 11 | 1.01 | 0.53 | 0.20 |
| PIM1_CHEMBL1022925 | 16 | 0.95 | 0.47 | 0.48 |
| PIM1_CHEMBL2038828 | 12 | 0.77 | 0.55 | 0.50 |
| PLA2G7_CHEMBL707410 | 23 | 1.09 | 0.40 | 0.53 |
| PPARD_CHEMBL759401 | 11 | 1.25 | 0.67 | 0.60 |
| PTGES_CHEMBL3999537 | 11 | 1.09 | 0.69 | 0.61 |
| Pka_hist | 8 | 0.51 | 0.87 | 0.79 |
| ROCK2_CHEMBL4669834 | 12 | 1.14 | 0.38 | 0.39 |
| RXRA_CHEMBL797916 | 10 | 0.99 | 0.64 | 0.64 |
| SLC5A2_CHEMBL1217373 | 10 | 1.07 | 0.56 | 0.69 |
| SRC_CHEMBL2039537 | 10 | 1.36 | 0.90 | 0.73 |
| STK3_CHEMBL3395732 | 8 | 0.71 | 0.42 | 0.64 |
| TA1_GPCRFEP | 8 | 1.07 | 0.58 | 0.43 |
| TNKS_CHEMBL2384487 | 9 | 0.72 | 0.84 | 0.87 |
| TRAP1_CHEMBL3427925 | 8 | 1.33 | 0.57 | 0.21 |
| TTK_CHEMBL3411333 | 25 | 0.86 | 0.74 | 0.73 |
| bace_jacs_set | 36 | 0.80 | 0.47 | 0.49 |
| beta1_GPCRFEP | 9 | 0.91 | 0.14 | 0.22 |
| brd41_ASH106-waterset | 8 | 0.66 | 0.62 | 0.79 |
| cdk2_jacs_set | 16 | 0.81 | 0.54 | 0.53 |
| cdk8_merck | 32 | 0.87 | 0.84 | 0.70 |
| chk1-waterset | 13 | 1.02 | 0.53 | 0.61 |
| cmet_merck | 24 | 1.01 | 0.79 | 0.73 |
| eg5_merck | 28 | 0.84 | 0.54 | 0.46 |
| hif2a_merck | 41 | 1.54 | 0.22 | 0.28 |
| hsp90_kung-waterset | 11 | 1.20 | 0.65 | 0.56 |
| hsp90_woodhead-waterset | 4 | 0.43 | 0.95 | 1.00 |
| jnk1_jacs_set | 21 | 0.65 | 0.59 | 0.63 |
| mGluR5_GPCRFEP | 12 | 1.16 | 0.73 | 0.79 |
| mGluR5_hist | 12 | 1.16 | 0.73 | 0.78 |
| mcl1_jacs_set | 42 | 1.19 | 0.57 | 0.57 |
| p38_jacs_set | 34 | 0.92 | 0.42 | 0.54 |
| pfkfb3_merck | 40 | 1.06 | 0.39 | 0.44 |
| ptp1b_jacs_set | 23 | 0.91 | 0.57 | 0.67 |
| scytalone_dehyd-waterset | 7 | 1.35 | 0.71 | 0.62 |
| shp2_merck | 26 | 1.79 | 0.04 | 0.12 |
| syk_merck | 48 | 1.56 | 0.26 | 0.42 |
| taf12-waterset | 8 | 0.46 | 0.67 | 0.36 |
| throm-waterset | 39 | 0.72 | 0.63 | 0.63 |
| thrombin_jacs_set | 11 | 0.78 | 0.66 | 0.64 |
| tnks2_merck | 33 | 1.03 | 0.24 | 0.28 |
| tyk2_jacs_set | 16 | 0.81 | 0.63 | 0.55 |
| urokinase-waterset | 4 | 0.55 | 0.60 | 1.00 |
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
3. **Ensure that the benchmark summary table is updated** by running:
   ```cmd
   python scripts/update_summary_table.py
   ```

This metadata should be included in the **Merge Request description**.

By following these guidelines, we ensure consistency across datasets and allow for fair comparisons between different versions of Uni-FEP.

