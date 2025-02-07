import numpy as np
import matplotlib.pyplot as plt
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

def generate_markdown_table(results):
    """Generate markdown table from results."""
    headers = ["System", "N_Ligands", "RMSE (kcal/mol)", "R²", "Kendall's tau"]
    table = ["| " + " | ".join(headers) + " |"]
    table.append("|" + "|".join(["---"] * len(headers)) + "|")
    
    for row in results[1:]:  # Skip header row
        formatted_row = [
            row[0], 
            str(row[1]), 
            f"{row[2]:.2f}",
            f"{row[3]:.2f}", 
            f"{row[4]:.2f}"
        ]
        table.append("| " + " | ".join(formatted_row) + " |")
    
    return "\n".join(table)

def update_readme(md_table, readme_path="README.md"):
    """Update the README file with new results table."""
    start_marker = "## Summary of Benchmark Results"
    end_marker = "## "
    
    with open(readme_path, "r") as f:
        content = f.read().split('\n')
    
    start_idx = next(i for i, line in enumerate(content) 
                    if start_marker in line) + 1
    end_idx = next(i for i, line in enumerate(content[start_idx:]) 
                 if line.startswith(end_marker)) + start_idx
    
    new_content = (
        content[:start_idx] +
        [md_table] + 
        content[end_idx:]
    )
    
    with open(readme_path, "w") as f:
        f.write("\n".join(new_content))

def main():
    # Initialize results table
    results = [
        ["System", "N_Ligands", "RMSE (kcal/mol)", "R²", "Kendall's tau"]
    ]
    
    # Process each benchmark system
    benchmarks_dir = Path("uni_fep_benchmarks")
    for system_dir in sorted(benchmarks_dir.iterdir()):
        if system_dir.is_dir():
            try:
                data_file = system_dir / "result_dG.csv"
                dG_pred, _, dG_expt = load_dG(data_file)
                rmse, r2, tau = calculate_metrics(dG_expt, dG_pred)
                
                results.append([
                    system_dir.name,
                    len(dG_pred),
                    rmse,
                    r2,
                    tau
                ])
            except Exception as e:
                print(f"Error processing {system_dir}: {str(e)}")
                continue
    
    # Generate and update markdown
    md_table = generate_markdown_table(results)
    update_readme(md_table)

if __name__ == "__main__":
    main()