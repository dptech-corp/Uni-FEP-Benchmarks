import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
from pathlib import Path
import csv

def load_dG(file_path):
    """Load free energy data from CSV file."""
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        items = list(reader)
        
        dG_pred = np.array([float(i['fep_dG (kcal/mol)']) for i in items])
        dG_expt = np.array([float(i['exp_dG (kcal/mol)']) for i in items])
        
        # Handle optional standard deviation column
        try:
            std_dG_pred = np.array([float(i['fep_dG_std (kcal/mol)']) for i in items])
        except KeyError:
            std_dG_pred = np.zeros_like(dG_pred)
            
    return dG_pred, std_dG_pred, dG_expt

def calculate_metrics(dG_expt, dG_pred):
    """Calculate validation metrics."""
    mse = np.mean((dG_expt - dG_pred)**2)
    rmse = np.sqrt(mse)
    r2 = np.corrcoef(dG_expt, dG_pred)[0, 1]**2
    tau, _ = stats.kendalltau(dG_expt, dG_pred)
    return rmse, r2, tau


def generate_scatter_plot(dG_expt, dG_pred, std_dG_pred, out_path):
    """Generate scatter plot comparing predicted vs experimental energies."""
    dG_min = min(np.min(dG_pred), np.min(dG_expt)) - 1.5
    dG_max = max(np.max(dG_pred), np.max(dG_expt)) + 1.5

    plt.figure(dpi=300, figsize=(6.5, 4.8))
    plt.plot([dG_min, dG_max], [dG_min, dG_max], '-', c='black')
    plt.fill_between(
        [dG_min, dG_max],
        [dG_min + 1, dG_max + 1],
        [dG_min - 1, dG_max - 1],
        color='gray',
        alpha=0.5,
        label='1 kcal/mol error',
    )
    plt.fill_between(
        [dG_min, dG_max],
        [dG_min + 2, dG_max + 2],
        [dG_min - 2, dG_max - 2],
        color='gray',
        alpha=0.2,
        label='2 kcal/mol error',
    )

    plt.errorbar(dG_expt, dG_pred, yerr=std_dG_pred, fmt='o', c='blue')
    plt.xlim(dG_min, dG_max)
    plt.ylim(dG_min, dG_max)
    plt.legend(edgecolor='none', fontsize='small')
    plt.xlabel('Experimental (kcal/mol)')
    plt.ylabel('Predicted (kcal/mol)')
    rmse, r2, tau = calculate_metrics(dG_expt, dG_pred)
    plt.title(
        f'RMSE: {rmse:.2f} kcal/mol,  R$^2$: {r2:.2f},  Kendall\'s tau: {tau:.2f}'
    )
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def generate_markdown_table(results):
    """Generate markdown table from results."""
    headers = ["Series", "Target", "N_Ligands", "RMSE (kcal/mol)", "R²", "Kendall's tau", "Description"]
    table = ["| " + " | ".join(headers) + " |"]
    table.append("|" + "|".join(["---"] * len(headers)) + "|")
    
    for row in results[1:]:  # Skip header row
        formatted_row = [
            str(row[0]), 
            str(row[1]),
            str(row[2]), 
            f"{row[3]:.2f}",
            f"{row[4]:.2f}", 
            f"{row[5]:.2f}",
            str(row[6])
        ]
        table.append("| " + " | ".join(formatted_row) + " |")
    
    return "\n".join(table)

def update_readme(
    md_table,
    num_targets,
    total_ligands,
    rmse_fig,
    tau_fig,
    readme_path="README.md",
):
    """Update the README file with summary information and results table."""
    start_marker = "## Summary of Benchmark Results"
    end_marker = "## "

    with open(readme_path, "r") as f:
        content = f.read().split("\n")

    start_idx = next(i for i, line in enumerate(content) if start_marker in line) + 1
    try:
        end_idx = (
            next(i for i, line in enumerate(content[start_idx:], start_idx) if line.startswith(end_marker))
        )
    except StopIteration:
        end_idx = len(content)

    summary_lines = [
        f"**Total Systems**: {num_targets}  ",
        f"**Total Ligands**: {total_ligands}",
        f"![RMSE Distribution]({rmse_fig})",
        f"![Kendall's tau Distribution]({tau_fig})",
        md_table,
    ]

    new_content = content[:start_idx] + summary_lines + content[end_idx:]

    with open(readme_path, "w") as f:
        f.write("\n".join(new_content))

def main():
    # Initialize containers
    results = [["System", "N_Ligands", "RMSE (kcal/mol)", "R²", "Kendall's tau"]]
    rmse_list = []
    tau_list = []
    total_ligands = 0

    # Process each benchmark system
    benchmarks_dir = Path("uni_fep_benchmarks")
    for system_dir in sorted(benchmarks_dir.iterdir()):
        if system_dir.is_dir():
            try:
                info = system_dir.name.split("|")
                series = info[0]
                target = info[1]
                description = info[2] if len(info) > 2 else ""

                data_file = system_dir / "result_dG.csv"
                dG_pred, std_dG_pred, dG_expt = load_dG(data_file)
                rmse, r2, tau = calculate_metrics(dG_expt, dG_pred)

                # update scatter figure
                fig_path = system_dir / "result_dG.png"
                generate_scatter_plot(dG_expt, dG_pred, std_dG_pred, fig_path)

                results.append(
                    [
                        series,
                        target,
                        len(dG_pred),
                        rmse,
                        r2,
                        tau,
                        description,
                    ]
                )
                rmse_list.append(rmse)
                tau_list.append(tau)
                total_ligands += len(dG_pred)
            except Exception as e:
                print(f"Error processing {system_dir}: {str(e)}")
                continue

    num_targets = len(results) - 1

    # Generate histogram figures
    df = pd.DataFrame({"RMSE (kcal/mol)": rmse_list, "Kendall's tau": tau_list})

    rmse_fig = "rmse_distribution.png"
    tau_fig = "tau_distribution.png"

    plt.figure(figsize=(10, 2), dpi=300)
    sns.histplot(df["RMSE (kcal/mol)"], bins=20, kde=True)
    plt.xlim(0, 2.5)
    plt.xlabel("RMSE (kcal/mol)", fontdict={"fontsize": 16, "fontname": "Serif"})
    plt.ylabel("System Count", fontdict={"fontsize": 16, "fontname": "Serif"})
    plt.grid(False)
    plt.tight_layout()
    plt.savefig(rmse_fig)
    plt.close()

    plt.figure(figsize=(10, 2), dpi=300)
    sns.histplot(df["Kendall's tau"], bins=20, kde=True)
    plt.xlim(0, 1)
    plt.xlabel("Kendall's tau", fontdict={"fontsize": 16, "fontname": "Serif"})
    plt.ylabel("System Count", fontdict={"fontsize": 16, "fontname": "Serif"})
    plt.grid(False)
    plt.tight_layout()
    plt.savefig(tau_fig)
    plt.close()

    # Generate markdown table and update README
    md_table = generate_markdown_table(results)
    update_readme(md_table, num_targets, total_ligands, rmse_fig, tau_fig)

if __name__ == "__main__":
    main()
