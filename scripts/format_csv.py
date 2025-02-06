import msys
from rdkit import Chem
import csv
import sys
from pathlib import Path


def mol_to_smiles(mol: msys.System) -> str:
    return Chem.MolToSmiles(msys.ConvertToRdkit(mol))


csv_file, sdf_file = sys.argv[1], sys.argv[2]
result_file = sys.argv[3]

mols = {
    m.name: m for m in msys.LoadMany(sdf_file)
}

with open(csv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)
    ligand_names = [i['mol'] for i in data]
    dG_pred = [float(i['dG_pred']) for i in data]
    dG_expt = [float(i['dG_expt']) for i in data]
    std_dG_pred = [float(i['std_dG_pred']) for i in data]

ligand_smiles = [
    mol_to_smiles(mols[name]) for name in ligand_names
]

result_path = Path(result_file)
result_path.parent.mkdir(parents=True, exist_ok=True)

with open(result_file, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ligand_smiles', 'ligand_name', 'exp_dG (kcal/mol)', 'fep_dG (kcal/mol)', 'fep_dG_std (kcal/mol)'])
    for i in range(len(ligand_names)):
        writer.writerow([ligand_smiles[i], ligand_names[i], dG_expt[i], dG_pred[i], std_dG_pred[i]])
