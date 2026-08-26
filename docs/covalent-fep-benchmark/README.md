# Covalent FEP Benchmark

Reversible-covalent relative binding free-energy (RBFE) benchmarks computed with Uni-FEP.

**5 systems, 47 ligands, 41 edges.** All campaigns: AM1-BCC (GAFF2), 5 ns/leg.

| Directory | Target | Warhead | Cys | Edges | n | Pearson R | RMSE |
|---|---|---|---|--:|--:|--:|--:|
| `Covalent\|hCatL\|Bonatto2021` | hCatL | nitrile | CYS25 | 6 | 8 | 0.685 | 0.859 |
| `Covalent\|hCatL\|Lameira2019` | hCatL | nitrile | CYS25 | 4 | 5 | 0.901 | 0.397 |
| `Covalent\|hCatL\|Hardegger2011` | hCatL | nitrile | CYS25 | 6 | 7 | -0.592 | 1.433 |
| `Covalent\|CAPN1\|Chatterjee1996` | CAPN1 | alpha-ketoamide | CYS115 | 6 | 7 | 0.131 | 0.700 |
| `Covalent\|CRUZAIN\|Avelar2015` | CRUZAIN | nitrile | CYS25 | 19 | 20 | 0.654 | 0.856 |

## Layout

Each system directory follows the `<SOURCE>|<TARGET>|<SERIES_ID>` convention and is flat, like every
other entry:

```
uni_fep_benchmarks/Covalent|hCatL|Bonatto2021/
protein.pdb        gap-filled receptor actually simulated
ref_ligand.sdf     covalent adduct of the reference ligand
result_dG.csv      ligand_smiles, ligand_name, exp_dG, fep_dG, fep_dG_std
result_dG.png      predicted vs experimental
edges.csv          per-edge ddG with BAR error (the primary RBFE observable)
pose_*.sdf         covalent adduct of each ligand, as used in the FEP
ligand_*.sdf       the corresponding free ligand
```

Warhead, covalent attachment residue, reference ligand and source DOI for every system are in
[`summary.csv`](summary.csv); the simulation protocol is in [`PROTOCOL.md`](PROTOCOL.md).
