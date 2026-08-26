# Simulation Protocol

## Common settings

All systems use the same engine settings; only the lambda ladder differs between mutation classes.

| Setting                                       | Value                                                               |
| --------------------------------------------- | ------------------------------------------------------------------- |
| Force field                                   | AMBER14SB / TIP3P, GAFF2 ligand                                     |
| Sampling                                      | Hamiltonian replica exchange (HREMD), 5 ns per lambda window        |
| Timestep                                      | 4 fs (hydrogen mass repartitioning)                                 |
| REST2 scale                                   | 1/3 at the middle of the ladder, 1.0 at both end states             |
| Water exchange                                | SwapMC enabled, 4 ps interval                                       |
| Adaptive lambda                               | disabled                                                            |
| Endpoint declash                              | enabled                                                             |
| Steric rotamer search (`auto_rotamer_select`) | **disabled** - see note below                                       |
| Legs                                          | vacuum, solvated, complex; ddG = dG(complex) - dG(solvated)         |
| Replicas                                      | 3 independent repeats (different random seeds) for 79 of 87 systems |

**Note on `auto_rotamer_select`.** This option performs a purely steric side-chain search with no
energy term and no rotamer library. Enabling it across the whole set degraded R2 from 0.42 to 0.16
and produced seven NaN failures, because it walks side chains off their rotamer wells and breaks
crystallographic polar contacts. It is disabled throughout.

## Why three mutation classes

Different mutations perturb different terms of the Hamiltonian, and they do not converge at the same
rate. Applying one lambda ladder to all of them either wastes sampling on the easy cases or
under-discretises the hard ones, so mutations are stratified into three classes, each with its own
ladder:

| Class | Definition                                | lambda windows | Rationale                                                                                                   |
| ----- | ----------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------- |
| **A** | neutral, small change or truncation       | **16**         | Only side-chain van der Waals and torsional terms are perturbed.                                            |
| **B** | neutral, growth or aromatic ring involved | **24**         | A larger dummy region must be grown or removed; ring systems add bonded and torsional terms.                |
| **C** | charge-changing                           | **40**         | Charge annihilation and creation require the finest discretisation.                                         |

### Known blind spot of the classifier

The classifier keys on volume change and net-charge change, so mutations that **swap one polar or
charged functional group for another** - His->Leu, Lys->Arg, Arg->Lys - are assigned to class A even
though they perturb the electrostatics substantially. Five systems fall in this category, and they
show the signature of an under-discretised ladder: replica-exchange acceptance drops below 0.05 in
some windows, and replica-to-replica scatter is large.

One of them, 2PQL H35L, appeared accurate in a single run (error -0.17 kcal/mol) but gave
-7.87 kcal/mol as a three-replica mean; re-running it with 24 windows returned +0.13 kcal/mol. When a
class-A mutation exchanges a polar or charged group, promote it to 24 windows rather than trusting
the automatic assignment.

## Enhanced protocol for difficult systems

Twelve systems in the main set did not reach the accuracy target under the baseline protocol. These
are structurally harder cases - large cavity creation, bulky residues grown into a packed pocket, or
loss of a buried hydrogen-bonding network - where the baseline's minimal REST2 region is
insufficient. For these we adopt a **more aggressive enhanced-sampling design**:

| Parameter                       | Baseline | Enhanced (`pocket-heating`)                                  |
| ------------------------------- | -------- | ------------------------------------------------------------ |
| `rest2_neighbor_cutoff`         | off      | 3.0 A around the mutation site                               |
| `rest2_pocket_ligand_cutoff`    | off      | 5.0 A around the ligand                                      |
| `rest2_pocket_full_hamiltonian` | off      | on (neutral pocket residues also enter the non-bonded boost) |

This widens the REST2 region from 3-18 heated atoms to 116-234, and - importantly - from 0-24 heated
atoms in the *mutant* end state to 114-245. Ten of the twelve improved and none regressed.

For two class-A systems the wider heated region also required more lambda windows to keep adjacent
windows overlapping (16 -> 24); these are labelled `pocket-heating+lambda`.

The per-system protocol is recorded in the `protocol` column of every `result_ddG.csv`.
