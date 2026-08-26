# Simulation protocol (Uni-FEP covalent RBFE)

## Chemistry / force field
- Protein: ff14SB; covalent cysteine typed as **CYX**
- Ligand: GAFF2 + **AM1-BCC** (`charge_method=bcc`)
- Junction bond/angles/dihedrals: parameterized on capped adduct (ACE–CYX–NME + ligand)
- Reference leg solute: capped cysteine model (ACE–CYX–NME), not the apo protein

## Mapping / REST2
- Atom mapping: covalent MCS mapping (`preserve_mcs`) between posed adducts
- REST2 strategy: **`dummy-extend`** (boost fragments that contain alchemical dummy atoms after cutting rotatable bridges)

## Sampling (production reported here)
- Per λ-window HREMD / Uni-FEP default schedule
- **5.0 ns** production per leg (vacuum / solvated / complex)
- Discard first **0.5 ns** in analysis (`skip=500 ps`)
- **No** adaptive equilibration (`run_*_adaptive=False`)
- Platform: `CUDA_MIXED`

## Analysis
- Pairwise BAR between adjacent λ windows, accumulated along the ladder → ΔG per leg
- Binding relative free energy: ΔΔG = ΔG_complex − ΔG_solvated
- Ligand absolute ΔG: weighted least-squares (MLE) on the edge graph with per-component gauge, then a global mean-shift to experimental ΔG (reports RMSE / R / Kendall τ)

## Edge graphs
See `edges.csv` in each system directory.
Bonatto/NEQ use literature stars; Calpain/Cruzain use star+bridges redesigns.
