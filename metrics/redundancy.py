import pandas as pd
import numpy as np

def redundancy_score(df: pd.DataFrame):

    warnings = []

    #Duplicate Rows
    total_rows = len(df)
    duplicate_rows = df.duplicated().sum()
    duplicate_ratio = duplicate_rows / total_rows if total_rows > 0 else 0

    if duplicate_ratio > 0.1:
        warnings.append(f"{duplicate_ratio:.0%} duplicate rows detected")

    #Highly Correlated Features (numeric only)
    numeric_df = df.select_dtypes(include=[np.number])

    high_corr_count = 0
    if numeric_df.shape[1] > 1:
        corr_matrix = numeric_df.corr().abs()
        upper_triangle = corr_matrix.where(
            np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
        )

        high_corr_pairs = [
            column for column in upper_triangle.columns
            if any(upper_triangle[column] > 0.9)
        ]

        high_corr_count = len(high_corr_pairs)

        if high_corr_count > 0:
            warnings.append(f"{high_corr_count} highly correlated feature(s) found")

    #Near-Constant Columns
    constant_cols = [
        col for col in df.columns
        if df[col].nunique() <= 1
    ]

    if constant_cols:
        warnings.append(f"{len(constant_cols)} near-constant column(s) detected")

    #Scoring Logic
    penalty = (
        duplicate_ratio * 5
        + high_corr_count * 1
        + len(constant_cols) * 1
    )

    score = max(0, 10 - penalty)
    score = round(score, 2)

    return {
        "score": score,
        "duplicate_ratio": round(duplicate_ratio, 3),
        "warnings": warnings
    }
