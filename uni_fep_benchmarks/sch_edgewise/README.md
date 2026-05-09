# sch_edgewise

Raw edge-level data underlying **Table S1** of:

> Zou, R.; Wang, L.; Wang, X.; Ding, Y.; Zheng, H.
> *Breaking Barriers in FEP Benchmarking: A Large-Scale Dataset Reflecting Real-World Drug Discovery Challenges.*
> ChemRxiv preprint, 2025. <https://chemrxiv.org/doi/10.26434/chemrxiv-2025-rf8mf>

Table S1 compares **Uni-FEP** against **FEP+** at the edgewise level on the Schrödinger benchmark set (Ross et al., *Commun Chem* 2023, 6, 222), using a single tautomer / protonation state / binding pose per ligand. The per-target RMSE and R² values reported in the table are aggregates of the per-edge predictions stored here.


## Columns

| Column | Description |
| --- | --- |
| `Type` | Benchmark category (e.g. `mcs_docking`, `jacs_set`, `merck`, `macrocycles`, `fragments`, `waterset`, `opls_stress`, `charge_annhil`, `scaffold_hopping`, `janssen_bace`, `misc`). |
| `Target` | Protein/system name within the category. |
| `mol1`, `mol2` | Ligand identifiers defining the perturbation edge (mol1 → mol2). |
| `ddG_pred` | Uni-FEP predicted relative binding free energy for the edge (kcal/mol). |
| `std_ddG_pred` | Uncertainty (std) of the predicted ddG (kcal/mol). |
| `ddG_expt` | Experimental relative binding free energy (kcal/mol). |
| `ddG_diff` | Absolute difference \|`ddG_pred` − `ddG_expt`\| (kcal/mol). |

## Reproducing Table S1 (Uni-FEP columns)

For each `(Type, Target)` group:

- `Uni-FEP_RMSE` = sqrt(mean((`ddG_pred` − `ddG_expt`)²))
- `Uni-FEP_R2` = R² of `ddG_pred` vs. `ddG_expt`

