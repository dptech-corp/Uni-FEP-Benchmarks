import numpy as np
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

def create_svg_hist(data, edges, filename, width=400, height=200):
    """Generate a simple histogram SVG using numpy."""
    counts, _ = np.histogram(data, bins=edges)
    max_count = counts.max() if counts.size else 0
    bar_width = width / len(counts)
    scale = (height - 20) / max_count if max_count > 0 else 0

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    ]
    for i, count in enumerate(counts):
        bar_h = count * scale
        x = i * bar_width
        y = height - bar_h
        lines.append(f'<rect x="{x}" y="{y}" width="{bar_width-2}" height="{bar_h}" fill="steelblue"/>')
        lines.append(
            f'<text x="{x + bar_width/2}" y="{height-5}" font-size="10" text-anchor="middle">{edges[i]:.1f}</text>'
        )
    lines.append('</svg>')

    Path(filename).write_text("\n".join(lines))

def build_summary_section(results):
    """Generate the text and images for the README summary section."""
    n_targets = len(results) - 1
    n_ligands = sum(row[2] for row in results[1:])

    rmses = [row[3] for row in results[1:]]
    taus = [row[5] for row in results[1:]]

    rmse_edges = np.arange(0, 2.5 + 0.5, 0.5)
    tau_edges = np.arange(0, 1.0 + 0.1, 0.1)

    rmse_hist = Path("docs/rmse_hist.svg")
    tau_hist = Path("docs/tau_hist.svg")
    create_svg_hist(rmses, rmse_edges, rmse_hist)
    create_svg_hist(taus, tau_edges, tau_hist)

    md_table = generate_markdown_table(results)

    lines = [
        f"Currently this repository contains **{n_targets}** targets and a total of **{n_ligands}** ligands.",
        "The histograms below summarize the distribution of RMSE and Kendall's tau values across all benchmark sets.",
        "",
        f"![RMSE distribution]({rmse_hist})",
        "",
        f"![Kendall's tau distribution]({tau_hist})",
        md_table,
    ]
    return "\n".join(lines)

def update_readme(summary_text, readme_path="README.md"):
    """Replace the summary section of the README with new content."""
    start_marker = "## Summary of Benchmark Results"
    end_marker = "## "
    
    with open(readme_path, "r") as f:
        content = f.read().split('\n')
    
    start_idx = next(i for i, line in enumerate(content) 
                    if start_marker in line) + 1
    end_idx = next(i for i, line in enumerate(content[start_idx:]) 
                 if line.startswith(end_marker)) + start_idx
    
    new_content = content[:start_idx] + [summary_text] + content[end_idx:]
    
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
                info = system_dir.name.split("|")
                series = info[0]
                target = info[1]
                if len(info) > 2:
                    description = info[2]
                else:
                    description = ""


                data_file = system_dir / "result_dG.csv"
                dG_pred, _, dG_expt = load_dG(data_file)
                rmse, r2, tau = calculate_metrics(dG_expt, dG_pred)
                
                results.append([
                    series,
                    target,
                    len(dG_pred),
                    rmse,
                    r2,
                    tau,
                    description
                ])
            except Exception as e:
                print(f"Error processing {system_dir}: {str(e)}")
                continue
    
    # Generate summary section and update README
    summary_text = build_summary_section(results)
    update_readme(summary_text)

if __name__ == "__main__":
    main()