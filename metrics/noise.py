import pandas as pd
import numpy as np


def noise_score(df: pd.DataFrame):

    warnings = []
    numeric_df = df.select_dtypes(include=[np.number])

    total_numeric_cols = len(numeric_df.columns)
    outlier_columns = 0

    # Outlier Detection using IQR
    for col in numeric_df.columns:

        Q1 = numeric_df[col].quantile(0.25)
        Q3 = numeric_df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = numeric_df[
            (numeric_df[col] < lower_bound) |
            (numeric_df[col] > upper_bound)
        ]

        if len(outliers) > 0.1 * len(df): 
             # >10% outliers
            outlier_columns += 1

    if outlier_columns > 0:
        warnings.append(f"{outlier_columns} column(s) contain excessive outliers")

    # High Variance Check
    high_variance_cols = 0

    for col in numeric_df.columns:
        if numeric_df[col].std() > numeric_df[col].mean() * 2:
            high_variance_cols += 1

    if high_variance_cols > 0:
        warnings.append(f"{high_variance_cols} column(s) show high variance instability")

    # Scoring Logic
    penalty = (outlier_columns * 2) + (high_variance_cols * 1.5)
    score = max(0, 10 - penalty)
    score = round(score, 2)

    return {
        "score": score,
        "warnings": warnings
    }
