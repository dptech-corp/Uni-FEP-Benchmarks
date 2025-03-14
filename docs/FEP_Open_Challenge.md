## FEP Open Challenge: Test and Validate Uni-FEP Performance

> Last Updated: 14/3/2025

### Project Overview
**FEP Open Challenge** is a long-term initiative hosted in the Uni-FEP-Benchmarks repository. We warmly invite researchers to test the accuracy and stability of Uni-FEP in free energy calculations, especially for those who have reservations about its performance. We encourage you to use your publicly available data or published datasets for comparative testing. Simultaneously, as the community conducts these tests, we will gradually build a public, fair, and transparent benchmark dataset. Our goal is to accumulate over 1,000 protein target-ligand complex benchmarks by the end of 2025 and share them with the global research community, thereby advancing FEP methodologies and drug activity prediction models across the field.

### Project Background
Free Energy Perturbation (FEP) methods are pivotal for optimizing lead compounds in drug discovery. However, debates persist regarding the accuracy, stability, and reproducibility of various FEP tools. To address these concerns, we launched the Uni-FEP Open Challenge within the Uni-FEP-Benchmarks repository. Our main objectives include:
- **Addressing Accuracy Concerns**: By performing Uni-FEP calculations based on the challenges provided by researchers and returning the test results, we aim to dispel any doubts about the stability and precision of Uni-FEP. 
- **Build an Open Benchmark Dataset**: Through the accumulation of validated test cases, we intend to establish a transparent and equitable benchmark dataset. This dataset will serve as a valuable resource for evaluating the performance of different FEP tools and methodologies.

### How to Participate
#### 1. Submit Your Test Case
Please create an issue in the Uni-FEP-Benchmarks repository using the dedicated submission template. Your submission should include the following files:
- **Protein Structure File (PDB)**: The 3D structural data of the target protein.
- **Reference Ligand File (SDF)**: The ligand used to identify the binding pocket.
- **Data File (CSV, SDF)**: The data file can be in CSV format (which should include molecular SMILES along with experimental activity) or in SDF format (containing experimental data). 
#### 2. Review and Evaluation
Each submitted test case will undergo both automated and manual review to ensure completeness and scientific rigor. Once approved, we will perform the FEP calculations and deliver the results back to you. Submissions that do not meet our quality criteria will be returned with feedback.
#### 3. Public Data and Results
All validated test cases and their corresponding Uni-FEP calculation results—as well as comparative data—will be published in the repository under the Apache 2.0 license. By submitting your test case, you agree to have your data and results shared publicly. This continuously updated benchmark dataset will serve as an objective and transparent platform for evaluating FEP performance, contributing significantly to the advancement of drug design technologies.
#### 4. Reward Policy
- Basic Reward: Participants who publicly post a comparison of Uni-FEP results with those of another commercial FEP tool for the same system-whether on a blog, X (Twitter), LinkedIn, a preprint, or in a journal article-will receive<sup>*</sup> **a $50 Amazon Gift Card**.
- Additional Reward: If the published results clearly show that the other commercial FEP tool significantly outperforms Uni-FEP, we will, upon verification, award **an additional $50 Amazon Gift Card** as a token of our appreciation.
*Subject to verification

### Project Guidelines and Considerations
- **Openness and Fairness**: All test cases and calculation results will be shared openly in the Uni-FEP-Benchmarks repository under the Apache 2.0 license, creating a robust and high-quality FEP benchmark dataset. Please anonymize any sensitive data before submission.
- **Intellectual Property Protection**: We strictly respect intellectual property rights. In future publications or technical reports utilizing data from this repository, we will appropriately acknowledge and include the contributions of all participants.
- **Long-Term Initiative**: This project is intended for ongoing participation with no fixed deadline. We encourage continuous contributions to progressively enhance the dataset.
- **Fair Participation**: To ensure equitable access to our resources and maintain a high standard of review, each individual is allowed to have only one active submission (issue) at a time. For collaborative projects, please designate a single representative to submit on behalf of your group.
- **Data Source Consideration**: We are already constructing FEP benchmarks from ChEMBL and BindingDB; therefore, we may avoid accepting cases sourced from these two datasets during our review process.
