import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import csv


def load_dG(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        items = list(reader)
        dG_pred = np.array([float(i['fep_dG (kcal/mol)']) for i in items])
        try:
            std_dG_pred = np.array([float(i['fep_dG_std (kcal/mol)']) for i in items])
        except:
            std_dG_pred = np.zeros(len(dG_pred))
        dG_expt = np.array([float(i['exp_dG (kcal/mol)']) for i in items])
    return dG_pred, std_dG_pred, dG_expt

def comp_val(dG_expt, dG_pred):
    # compute RMSE, R2 and Kendall's tau
    rmse = np.sqrt(np.mean((dG_expt - dG_pred)**2))
    r2 = np.corrcoef(dG_expt, dG_pred)[0, 1]**2
    tau, _ = stats.kendalltau(dG_expt, dG_pred)
    return rmse, r2, tau


dG_pred, std_dG_pred, dG_expt = load_dG(f'result_dG.csv')

dG_min = min([min(dG_pred), min(dG_expt)])
dG_max = max([max(dG_pred), max(dG_expt)])
dG_min = dG_min - 1.5
dG_max = dG_max + 1.5

plt.figure(dpi=300, figsize=(6.5, 4.8))
plt.plot([dG_min, dG_max], [dG_min, dG_max], '-', c='black')
plt.fill_between([dG_min, dG_max], [dG_min+1, dG_max+1], [dG_min-1, dG_max-1], color='gray', alpha=0.5, label='1 kcal/mol error')
plt.fill_between([dG_min, dG_max], [dG_min+2, dG_max+2], [dG_min-2, dG_max-2], color='gray', alpha=0.2, label='2 kcal/mol error')

plt.errorbar(dG_expt, dG_pred, yerr=std_dG_pred, fmt='o', c='blue')
plt.xlim(dG_min, dG_max)
plt.ylim(dG_min, dG_max)
plt.legend(edgecolor='none', fontsize='small')
plt.xlabel('Experimental (kcal/mol)')
plt.ylabel('Predicted (kcal/mol)')
rmse, r2, tau = comp_val(dG_expt, dG_pred)
plt.title(f'RMSE: {rmse:.2f} kcal/mol,  R$^2$: {r2:.2f},  Kendall\'s tau: {tau:.2f}')
plt.tight_layout()
plt.savefig('result_dG.png')