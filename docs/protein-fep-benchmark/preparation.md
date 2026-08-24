# Structure Preparation

## Pipeline

Receptors were prepared with **fepfixer** in ligand-aware mode: missing residues and side chains are
rebuilt, protonation states are assigned by PROPKA at the experimental pH with the ligand present,
disulfides are detected, and the hydrogen-bond network is optimised. Ligands were taken from the
Aldeghi supplementary data (GAFF2/RESP parameters).

Note that the source dataset contains **no crystallographic waters**; all solvent in these
calculations is placed by the solvation step.

## Manual repairs

Eight systems required corrections to the prepared structure. These change only the input
coordinates - the simulation protocol is unchanged - so the repaired structure is deposited as
`protein.pdb` and no separate protocol label is used.

| Target     | Repair                                                             | Rationale                                                                                                                                                                                                               |
| ---------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1YON       | ASN180, ASN184 amide flip                                          | Flipped orientation scored -2.0 against +1.0 for the alternative; both residues sit within 5 A of the ligand                                                                                                            |
| 1YON       | GLH256 carboxyl proton reoriented (225 deg about Cdelta-Oepsilon2) | The proton pointed away from the ligand (O-H...O angle 49 deg), leaving a 2.35 A acceptor-acceptor contact; after reorientation the angle is 171 deg                                                                    |
| 2PQL       | ASN8 amide flip                                                    | Adjacent to the mutated GLU7; score -2.0 -> +2.0                                                                                                                                                                        |
| 3RDQ       | GLN107 amide flip                                                  | Adjacent to the mutated VAL108                                                                                                                                                                                          |
| 1AMW       | ASN37 amide flip                                                   | Direct ligand contact at 2.9 A; score -5.0 -> +4.0, the largest improvement in the set                                                                                                                                  |
| 1AMW, 2YGE | redundant chain removed                                            | The second chain of the crystallographic dimer lies 14-23 A from both the ligand and the mutation site and carries no ligand of its own; removing it reduces the water count by ~63% with no change to the computed ddG |
| 2PDP       | ARG302 side chain reoriented (chi3 180 deg, chi4 260 deg)          | All three guanidinium nitrogens made no hydrogen bond in the deposited model; the rotamer chosen forms one backbone and two water contacts with no steric clash                                                         |
| 3ZY2       | ARG40 side chain reoriented (chi3 30 deg, chi4 90 deg)             | As above; the chosen rotamer donates to a GDP phosphate oxygen at 2.87 A                                                                                                                                                |

The amide-flip and redundant-chain checks are objective and can be applied automatically before any
simulation is run. The two arginine reorientations are a weaker intervention: without electron
density we cannot confirm that the deposited rotamer is wrong, only that a charged guanidinium making
no hydrogen bond in a pocket with available acceptors is physically implausible. Their effect was
mixed - one system improved, one degraded - and they are reported here for transparency rather than
recommended as a general procedure.
