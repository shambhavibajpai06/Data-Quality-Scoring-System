📊 Data Quality Scoring System

An automated system that evaluates how suitable a dataset is for Machine Learning by assigning a Data Quality Score (0–10) along with detailed metric breakdown and actionable warnings.

🚀 Why This Project?

Most ML failures occur due to poor data quality, not bad models.

This tool helps:

-Detect missing data issues

-Identify redundancy

-Analyze class imbalance and bias

-Provide explainable scoring

-Assess ML-readiness before model training

🧠 Features
1️⃣ Missing Value Analysis

-Percentage of missing cells

-Column-level missing warnings

-Completeness score

2️⃣ Redundancy Detection

-Duplicate row detection

-Highly correlated features

-Near-constant columns

3️⃣ Bias Detection

-Class imbalance detection

-Entropy-based skew measurement

-Fairness risk warnings


📂 Project Structure
data-quality-scoring-system/
│
├── metrics/
│   ├── missing.py
│   ├── redundancy.py
│   └── bias.py
│
├── main.py
├── score_engine.py
├── sample.csv
├── requirements.txt
└── README.md

⚙️ Installation

1.Clone the repository:

git clone <your-repo-url>
cd data-quality-scoring-system


2.Install dependencies:

pip install -r requirements.txt

▶️ How to Use
Step 1: Place Your Dataset

Put your CSV file inside the project root folder
(or provide full path to the file).

Example: sample.csv

Step 2: Run the Tool
✅ With Bias Analysis (Recommended)
python main.py --file sample.csv --target department

--file → Path to dataset (required)
--target → Target column name for bias analysis (optional but recommended)

Example: python main.py --file sample.csv --target label

✅ Without Bias Analysis

If your dataset has no target column: python main.py --file sample.csv

🎯 Scoring Philosophy

Each metric produces a score between 0–10.
Final readiness can be extended using weighted aggregation.

This system emphasizes:

-Explainability

-Fairness awareness

-Practical ML usability

🏆 Ideal Use Cases

-ML project pre-check

-Dataset validation before training

-Academic research

-Data auditing

