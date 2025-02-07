# GCKR System FEP Calculation Results Analysis

## Target Introduction

GCKR (Glucokinase Regulatory Protein) is a key metabolic regulator that plays a crucial role in glucose homeostasis by modulating the activity of glucokinase (GK), the primary glucose sensor in hepatocytes. It functions as a competitive inhibitor of glucokinase in low glucose conditions and releases it when glucose levels rise. GCKR has emerged as an important therapeutic target for type 2 diabetes and related metabolic disorders, as its modulation can affect hepatic glucose metabolism and lipid homeostasis. The development of GCKR modulators represents a promising approach for treating metabolic diseases.

## Dataset Analysis

![Molecular structures of representative compounds](mol_grid.png)

The GCKR system dataset in this study comprises 11 compounds, sharing a similar structural framework with the previous GCKR dataset but tested under different assay conditions. These compounds feature a thiophene-benzene core linked to a pyridine ring, with various substituents including chloro-substituted phenyl rings and cyclopropylsulfonamide groups. The compounds demonstrate structural diversity through different modifications at the pyridine terminus and varying substitution patterns on the aromatic rings.

The experimentally determined binding affinities range from 3.8 nM to 4400.0 nM, spanning approximately three orders of magnitude, with binding free energies from -7.30 to -11.48 kcal/mol.

## Conclusions

The FEP calculation results for this GCKR system demonstrate excellent predictive performance with an R² of 0.87 and an RMSE of 0.74 kcal/mol. The predicted binding free energies (-6.66 to -12.28 kcal/mol) show strong correlation with experimental values. Several compounds showed excellent prediction accuracy, such as CHEMBL3745752 (experimental: -8.89 kcal/mol, predicted: -8.89 kcal/mol) and CHEMBL3746846 (experimental: -7.30 kcal/mol, predicted: -7.28 kcal/mol). The most potent compound, CHEMBL3746243, with an experimental binding free energy of -11.48 kcal/mol, was well predicted at -11.39 kcal/mol.

## References

For more information about the GCKR target and associated bioactivity data, please visit:
https://www.ebi.ac.uk/chembl/explore/assay/CHEMBL3751192 