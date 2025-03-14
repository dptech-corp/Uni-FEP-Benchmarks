---
name: FEP Open Challenge Submission
about: Submit a test case to evaluate Uni-FEP.
title: "[Challenge] Protein-Target_Name - Ligand_Set_Name"
labels: FEP Open Challenge
assignees: rongfengzou

---

## 🏆 FEP Open Challenge Submission

### 📌 Test Case Summary
_Provide a brief description of your test case._
> Example: This test case evaluates Uni-FEP's accuracy in predicting binding affinities for kinase inhibitors.

### 📝 Data Source
_Provide the source of your dataset (e.g., literature, publicly available in-house experimental data, etc.)._
> Example: DOI of the original paper or mention if it's unpublished data.


### 📂 Data Files
#### 📁 1. Protein Structure File (PDB)
_Upload or link to the PDB file containing the protein structure._
- **File Name:** `[Insert file name]`
- **Description:** _Provide details about the protein structure (e.g., resolution, source, modifications, binding pocket information)._
> Example: "PDB structure from PDB ID: 6LU7, modified to include missing loops."

#### 📁 2. Reference Ligand File (SDF)
_Upload or link to the SDF file containing the reference ligand._
- **File Name:** `[Insert file name]`
- **Description:** _Describe the reference ligand (e.g., known binder, co-crystalized ligand, binding mode)._
> Example: "Reference ligand extracted from PDB 6LU7, used to define the binding pocket."

#### 📁 3. Data File (CSV/SDF)
_Upload or link to the dataset file (CSV containing SMILES and experimental activity, or SDF containing experimental data)._
- **File Name:** `[Insert file name]`
- **Description:** _Explain the content (e.g., ligand structures, experimental binding affinities, logIC50/IC50 values)._
> Example: "CSV file with experimental IC50 values from published dataset (DOI: xxx)."

### 📬 Additional Comments
_Any additional information you would like to provide?_

---

### Important Notes:
- **Data Publication Consent**: By submitting this issue, you agree that your test case and calculation results will be published in the Uni-FEP-Benchmarks repository under the Apache 2.0 license.
- **Single Active Submission Policy**: To ensure fair participation, each individual is allowed only one active submission (issue) at a time.
- **Data Source Consideration**: Please note that submissions sourced from ChEMBL or BindingDB may not be accepted, as we are in the process of constructing our own benchmark dataset from these sources.
- **Sensitive Data**: If your data contains proprietary or sensitive information, please contact us before submission to discuss alternative methods.