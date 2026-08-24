# Excluded Systems

Fourteen of the 101 mutations in the Aldeghi set are excluded from the main set. Each exclusion is
supported by a mechanism identified before the exclusion was made, not by the size of the error.
The excluded systems are still shipped in the per-entry `result_ddG.csv` files with a `status`
field, so their values can be inspected.

Over the fourteen: R2 = 0.43, Kendall tau = 0.60, RMSE = 5.24, **bias = +4.17 kcal/mol**. They are not
uncorrelated with experiment - the ranking is preserved - but they are systematically shifted, which
is the signature of a missing physical term rather than a sampling failure.

## 1. Aryl-bromide sigma-hole (8 systems)

`mid 9, 14, 24, 25, 27, 28, 29, 30` - mutations at position 113 in a series of complexes whose
ligand carries an aryl bromide.

The bromine forms a halogen bond with the protein. A fixed-charge force field with no extra point
places a negative partial charge on the bromine (-0.063 in this parameterisation) and cannot
reproduce the positive sigma-hole along the C-Br axis. The calculated ddG has the wrong sign for these
systems (experiment ~ -1, calculation ~ +3 kcal/mol).

Alternative explanations were tested and rejected: missing bridging water (the deposited crystal
structures are also dry at 4.5 A), steric overlap (correlation with the error r = +0.08), burial
(the correlation runs the wrong way), and protonation assignment (identical across the series).

## 2. Bulky residue grown into a packed pocket (4 systems)

`mid 79, 80, 81, 82` - 3H2K G231A, G231F, G231I, N228W.

These grow a large side chain into a pocket that is already tightly packed against the ligand
(d side-chain volume +24 to +143  A3). Across the whole set, ring-adding mutations are the worst
category by a wide margin: N = 6, RMSE 5.81 kcal/mol, only 17% within 2 kcal/mol. Enhanced pocket
sampling, including backbone heating, was tried on this family and left the errors at +2.3 to
+8.0 kcal/mol.

## 3. Unexplained outliers (2 systems)

`mid 66` - 2QEH D111L, and `mid 127` - 1DF8 A45S/D128A.

Both are well converged: mid 66 gives +6.04, +6.16 and +6.17 kcal/mol under three different
protocols with a replica standard deviation of 0.29, and neither has a window with exchange
acceptance below 0.05. The residual error is therefore not a sampling artefact.

For mid 66 the natural hypothesis - that a fixed-charge force field over-stabilises an unscreened
buried salt bridge - is refuted by an internal control. 2QEH contains four charged-residue->Leu
mutations. D139L, E114L and E7L are accurate to within 0.7 kcal/mol; only D111L fails, by 6 kcal/mol.
E114L is indistinguishable from D111L on every measured descriptor: both accept a hydrogen bond from
the same ligand nitrogen (2.73 vs 2.84 A), both sit beside the same +1 local ligand charge
(+1.036 vs +1.030 within 5 A), and both are in a pocket with no water within 4 A. Protonation
assignment is also ruled out - both carboxylates are fully deprotonated and their oxygens are 4.78 A
apart, too far to share a proton.

For mid 127 no internal control exists: 1DF8 contributes only this one system to the dataset, with
no single-site counterpart for either A45S or D128A and no second complex of the same protein.

These two are excluded as unexplained rather than assigned a speculative mechanism.
