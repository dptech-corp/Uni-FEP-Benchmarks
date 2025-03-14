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

## FEP Open Challenge
We are excited to announce the **FEP Open Challenge** – an initiative aimed at validating the accuracy and stability of Uni-FEP through community participation. Researchers are invited to submit their own test cases using publicly available or published datasets. Our team will perform the FEP calculations on the submitted data and return the results, helping to dispel any doubts about Uni-FEP's performance.

Key points of the challenge include:

- **Data-Driven Validation**: Submit your test case (including a protein structure, reference ligand, and dataset file), and our team will evaluate it to verify Uni-FEP’s precision.
- **Public Benchmarking**: All validated test cases and their results will be shared openly in the Uni-FEP-Benchmarks repository under the Apache 2.0 license, contributing to a transparent and high-quality benchmark dataset.
- **Reward Policy**: Publicly compare Uni-FEP with another commercial FEP tool under identical conditions using supporting evidence (e.g., via a preprint, blog, or journal article) to earn **a $50 Amazon Gift Card**—with **an additional $50** awarded upon verification if the other tool is shown to significantly outperform Uni-FEP.
- **Participation Guidelines**: To ensure fairness, each individual may only have one active submission at a time. Also, cases sourced from ChEMBL or BindingDB may be avoided during our review process.

For more details, please refer to our [FEP Open Challenge introduction](https://github.com/dptech-corp/Uni-FEP-Benchmarks/blob/main/docs/FEP_Open_Challenge.md).


## Summary of Benchmark Results
| Series | Target | N_Ligands | RMSE (kcal/mol) | R² | Kendall's tau | Description |
|---|---|---|---|---|---|---|
| ChEMBL | AKR1C3 | 11 | 0.90 | 0.59 | 0.67 | CHEMBL4428988 |
| ChEMBL | AMPD2 | 14 | 1.36 | 0.54 | 0.46 | CHEMBL5240593 |
| ChEMBL | AURKA | 7 | 1.12 | 0.79 | 0.59 | CHEMBL2382841 |
| ChEMBL | BACE1 | 10 | 0.96 | 0.89 | 0.91 | CHEMBL2352381 |
| ChEMBL | BRD4 | 12 | 0.48 | 0.77 | 0.34 | CHEMBL2183681 |
| ChEMBL | BRD4 | 13 | 0.55 | 0.89 | 0.53 | CHEMBL2433591 |
| ChEMBL | BRD4 | 26 | 0.68 | 0.50 | 0.60 | CHEMBL3414207 |
| ChEMBL | BRD4 | 109 | 0.71 | 0.47 | 0.52 | CHEMBL3706176 |
| ChEMBL | BRD4 | 29 | 1.08 | 0.63 | 0.57 | CHEMBL4020217 |
| ChEMBL | BRD4 | 21 | 1.16 | 0.29 | 0.31 | CHEMBL4200424 |
| ChEMBL | BRD4 | 28 | 1.18 | 0.26 | 0.22 | CHEMBL4308744 |
| ChEMBL | BRD4 | 25 | 0.73 | 0.36 | 0.45 | CHEMBL4310223 |
| ChEMBL | BRD4 | 24 | 0.66 | 0.40 | 0.53 | CHEMBL5037307 |
| ChEMBL | BRD4 | 26 | 0.89 | 0.47 | 0.50 | CHEMBL5044553 |
| ChEMBL | BRD4 | 36 | 0.76 | 0.49 | 0.50 | CHEMBL5137805 |
| ChEMBL | BRPF1 | 17 | 0.65 | 0.60 | 0.62 | CHEMBL3385101 |
| ChEMBL | CDK2 | 12 | 1.21 | 0.37 | 0.21 | CHEMBL2013356 |
| ChEMBL | CMA1 | 9 | 0.90 | 0.67 | 0.50 | CHEMBL4182330 |
| ChEMBL | CREBBP | 12 | 0.56 | 0.91 | 0.82 | CHEMBL3817157 |
| ChEMBL | CSNK1D | 13 | 1.48 | 0.47 | 0.50 | CHEMBL2211470 |
| ChEMBL | DOT1L | 8 | 2.29 | 0.90 | 0.79 | CHEMBL4480297 |
| ChEMBL | DPP4 | 23 | 0.74 | 0.61 | 0.50 | CHEMBL951312 |
| ChEMBL | DUT | 13 | 1.10 | 0.40 | 0.49 | CHEMBL2060493 |
| ChEMBL | EIF2AK3 | 12 | 1.17 | 0.65 | 0.60 | CHEMBL2444392 |
| ChEMBL | F10 | 14 | 1.13 | 0.63 | 0.67 | CHEMBL661585 |
| ChEMBL | F10 | 13 | 0.85 | 0.41 | 0.51 | CHEMBL661586 |
| ChEMBL | F2 | 16 | 0.84 | 0.65 | 0.58 | CHEMBL1067528 |
| ChEMBL | FKBP1A | 10 | 0.70 | 0.66 | 0.42 | CHEMBL678145 |
| ChEMBL | GAK | 21 | 1.11 | 0.63 | 0.56 | CHEMBL4736826 |
| ChEMBL | GCKR | 11 | 0.69 | 0.87 | 0.67 | CHEMBL3751185 |
| ChEMBL | GCKR | 11 | 0.74 | 0.87 | 0.67 | CHEMBL3751192 |
| ChEMBL | HSP90AA1 | 9 | 0.99 | 0.62 | 0.67 | CHEMBL3427922 |
| ChEMBL | IGF1R | 9 | 1.08 | 0.38 | 0.54 | CHEMBL1045057 |
| ChEMBL | JAK1 | 10 | 0.51 | 0.65 | 0.72 | CHEMBL4620434 |
| ChEMBL | JAK2 | 15 | 0.84 | 0.42 | 0.45 | CHEMBL3625473 |
| ChEMBL | JAK2 | 12 | 0.69 | 0.60 | 0.42 | CHEMBL3627422 |
| ChEMBL | JAK2 | 15 | 0.83 | 0.55 | 0.44 | CHEMBL4150584 |
| ChEMBL | KIF11 | 14 | 0.70 | 0.61 | 0.59 | CHEMBL1037992 |
| ChEMBL | KIF11 | 22 | 1.10 | 0.58 | 0.62 | CHEMBL1694081 |
| ChEMBL | KLK3 | 26 | 1.01 | 0.61 | 0.64 | CHEMBL4844448 |
| ChEMBL | LCK | 11 | 0.59 | 0.74 | 0.64 | CHEMBL903614 |
| ChEMBL | MAOB | 7 | 1.67 | 0.61 | 0.43 | CHEMBL3588480 |
| ChEMBL | MAP4K4 | 15 | 0.53 | 0.75 | 0.62 | CHEMBL3755426 |
| ChEMBL | MAPK14 | 8 | 0.65 | 0.66 | 0.50 | CHEMBL1101788 |
| ChEMBL | MAPK14 | 18 | 1.30 | 0.70 | 0.37 | CHEMBL1787752 |
| ChEMBL | MAPK14 | 11 | 1.47 | 0.45 | 0.70 | CHEMBL2061259 |
| ChEMBL | MELK | 13 | 0.91 | 0.57 | 0.35 | CHEMBL3824963 |
| ChEMBL | MELK | 8 | 0.79 | 0.72 | 0.62 | CHEMBL4006633 |
| ChEMBL | MET | 8 | 1.05 | 0.90 | 0.79 | CHEMBL2032485 |
| ChEMBL | MMP13 | 13 | 1.22 | 0.83 | 0.58 | CHEMBL1798873 |
| ChEMBL | NEK2 | 11 | 1.12 | 0.35 | 0.45 | CHEMBL1693342 |
| ChEMBL | NR1H2 | 8 | 1.61 | 0.63 | 0.64 | CHEMBL907758 |
| ChEMBL | PDE1B | 13 | 1.16 | 0.51 | 0.53 | CHEMBL4011522 |
| ChEMBL | PDE4B | 13 | 0.62 | 0.79 | 0.68 | CHEMBL3374901 |
| ChEMBL | PDE4D | 12 | 1.05 | 0.55 | 0.61 | CHEMBL3374902 |
| ChEMBL | PDE5A | 14 | 0.80 | 0.48 | 0.54 | CHEMBL968866 |
| ChEMBL | PDK2 | 20 | 0.45 | 0.88 | 0.82 | CHEMBL5057865 |
| ChEMBL | PDPK1 | 11 | 1.01 | 0.53 | 0.20 | CHEMBL1942054 |
| ChEMBL | PIM1 | 16 | 0.95 | 0.47 | 0.48 | CHEMBL1022925 |
| ChEMBL | PIM1 | 12 | 0.77 | 0.55 | 0.50 | CHEMBL2038828 |
| ChEMBL | PLA2G7 | 23 | 1.09 | 0.40 | 0.53 | CHEMBL707410 |
| ChEMBL | PPARD | 11 | 1.25 | 0.67 | 0.60 | CHEMBL759401 |
| ChEMBL | PTGES | 11 | 1.09 | 0.69 | 0.61 | CHEMBL3999537 |
| ChEMBL | ROCK2 | 12 | 1.14 | 0.38 | 0.39 | CHEMBL4669834 |
| ChEMBL | RXRA | 10 | 0.99 | 0.64 | 0.64 | CHEMBL797916 |
| ChEMBL | SLC5A2 | 10 | 1.07 | 0.56 | 0.69 | CHEMBL1217373 |
| ChEMBL | SRC | 10 | 1.36 | 0.90 | 0.73 | CHEMBL2039537 |
| ChEMBL | STK3 | 8 | 0.71 | 0.42 | 0.64 | CHEMBL3395732 |
| ChEMBL | TNKS | 9 | 0.72 | 0.84 | 0.87 | CHEMBL2384487 |
| ChEMBL | TRAP1 | 8 | 1.33 | 0.57 | 0.21 | CHEMBL3427925 |
| ChEMBL | TTK | 25 | 0.86 | 0.74 | 0.73 | CHEMBL3411333 |
| CyclicPeptide | Menin | 16 | 0.90 | 0.46 | 0.50 |  |
| CyclicPeptide | PCSK9 | 18 | 0.77 | 0.51 | 0.47 |  |
| GPCR | A2A | 10 | 0.76 | 0.83 | 0.69 | Deflorian |
| GPCR | A2A | 7 | 0.54 | 0.84 | 0.62 | Lenselink |
| GPCR | A2A | 9 | 0.91 | 0.50 | 0.39 | Minetti |
| GPCR | A2A | 7 | 0.38 | 0.33 | 0.62 | Piersanti |
| GPCR | CXCR4 | 9 | 1.11 | 0.44 | 0.25 |  |
| GPCR | D3 | 6 | 1.09 | 0.67 | 0.87 |  |
| GPCR | DOR | 11 | 0.83 | 0.59 | 0.60 |  |
| GPCR | OX2-set1 | 27 | 0.88 | 0.57 | 0.57 |  |
| GPCR | OX2-set2 | 24 | 1.07 | 0.25 | 0.35 |  |
| GPCR | TA1 | 8 | 1.07 | 0.58 | 0.43 |  |
| GPCR | beta1 | 9 | 0.91 | 0.14 | 0.22 |  |
| GPCR | mGluR5 | 12 | 1.16 | 0.73 | 0.79 |  |
| Hermite | 3CLPro | 5 | 0.83 | 0.69 | 0.80 |  |
| Hermite | ACK1 | 6 | 1.10 | 0.71 | 0.60 |  |
| Hermite | BCL6 | 6 | 1.01 | 0.84 | 0.60 |  |
| Hermite | CDK4 | 6 | 0.38 | 0.84 | 0.87 |  |
| Hermite | Eg5 | 7 | 0.40 | 0.58 | 0.52 |  |
| Hermite | FKBP12 | 6 | 0.53 | 0.84 | 0.87 |  |
| Hermite | FXR | 6 | 0.69 | 0.69 | 0.60 |  |
| Hermite | Galectin-3 | 8 | 0.90 | 0.89 | 0.93 |  |
| Hermite | HNE | 6 | 1.28 | 0.96 | 0.73 |  |
| Hermite | HSP90 | 11 | 1.29 | 0.71 | 0.73 |  |
| Hermite | KRAS-G12D | 10 | 0.76 | 0.91 | 0.87 |  |
| Hermite | PAK4 | 10 | 0.58 | 0.66 | 0.64 |  |
| Hermite | Pka | 8 | 0.51 | 0.87 | 0.79 |  |
| Hermite | mGluR5 | 12 | 1.16 | 0.73 | 0.78 |  |
| JACS8 | BACE | 36 | 0.80 | 0.47 | 0.49 |  |
| JACS8 | CDK2 | 16 | 0.81 | 0.54 | 0.53 |  |
| JACS8 | JNK1 | 21 | 0.65 | 0.59 | 0.63 |  |
| JACS8 | MCL1 | 42 | 1.19 | 0.57 | 0.57 |  |
| JACS8 | P38 | 34 | 0.92 | 0.42 | 0.54 |  |
| JACS8 | PTP1B | 23 | 0.91 | 0.57 | 0.67 |  |
| JACS8 | TYK2 | 16 | 0.81 | 0.63 | 0.55 |  |
| JACS8 | Thrombin | 11 | 0.78 | 0.66 | 0.64 |  |
| Merck8 | CDK8 | 32 | 0.87 | 0.84 | 0.70 |  |
| Merck8 | EG5 | 28 | 0.84 | 0.54 | 0.46 |  |
| Merck8 | HIF-2α | 41 | 1.54 | 0.22 | 0.28 |  |
| Merck8 | PFKFB3 | 40 | 1.06 | 0.39 | 0.44 |  |
| Merck8 | SHP2 | 26 | 1.79 | 0.04 | 0.12 |  |
| Merck8 | SYK | 48 | 1.56 | 0.26 | 0.42 |  |
| Merck8 | TNKS2 | 33 | 1.03 | 0.24 | 0.28 |  |
| Merck8 | c-Met | 24 | 1.01 | 0.79 | 0.73 |  |
| WaterSet | Brd4(1)-ASH106 | 8 | 0.66 | 0.62 | 0.79 |  |
| WaterSet | Chk1 | 13 | 1.02 | 0.53 | 0.61 |  |
| WaterSet | HSP90 | 11 | 1.20 | 0.65 | 0.56 | Kung |
| WaterSet | HSP90 | 4 | 0.43 | 0.95 | 1.00 | Woodhead |
| WaterSet | Scytalone-Dehydratase | 7 | 1.35 | 0.71 | 0.62 |  |
| WaterSet | Taf1(2) | 8 | 0.46 | 0.67 | 0.36 |  |
| WaterSet | Thrombin | 21 | 0.79 | 0.56 | 0.58 |  |
| WaterSet | Urokinase | 4 | 0.55 | 0.60 | 1.00 |  |
## Repository Structure

Each system is organized into a separate folder, containing:

```
scripts/
└── gen_figure.py       # Script for generating dG comparison plots based on result_dG.csv

uni_fep_benchmarks/
│── system_1/  
│   ├── README.md        # Brief description of the system  
│   ├── protein.pdb      # Protein structure file in PDB format  
│   ├── ref_ligand.sdf   # Reference ligand file in SDF format  
│   ├── result_dG.png    # Visualization of FEP-calculated dG  
│   ├── result_dG.csv    # Numerical results of dG comparisons  
│  
│── system_2/  
│   ├── README.md  
│   ├── protein.pdb     
│   ├── ref_ligand.sdf  
│   ├── result_dG.png  
│   ├── result_dG.csv  
│  
└── ...
```

## File Descriptions

- **`README.md`**: Contains a brief summary of the system, including error statistics (e.g., RMSE of dG and ddG).
- **`protein.pdb`**: The protein structure file in PDB format required for FEP calculations.
- **`ref_ligand.sdf`**: The reference ligand file in SDF format used to define the ligand in the system.
- **`result_dG.png`**: Graphical representation of **FEP-derived binding free energies (dG)** compared to experimental values.
- **`result_dG.csv`**: A table containing RBFE-predicted binding free energies (`fep_dG`) and experimental measurements (`exp_dG`).

#### `result_dG.csv` Example (RBFE-calculated dG values)
| ligand_smiles | ligand_name | exp_dG (kcal/mol) | fep_dG (kcal/mol) | fep_dG_std (kcal/mol) |
|----------------|--------------|-----------------|-----------------|-----------------|
| 'Ligand_SMILES' | 'Ligand_Name' | -7.5 | -7.2 | 0.15 |
| 'Ligand_SMILES' | 'Ligand_Name' | -8.1 | -7.9 | 0.08 |

## Data Update Guidelines

When submitting new benchmark data via a **Merge Request**, please provide the following:

1. Name all new folders using the format `Series|Target|Description`.
2. Include the required files in each system folder: `protein.pdb` and `ref_ligand.sdf` along with the existing files.
3. Update the benchmark summary table by running:
   ```cmd
   python scripts/update_summary_table.py
   ```

