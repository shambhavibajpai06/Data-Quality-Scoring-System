import pandas as pd

def missing_score(df: pd.DataFrame):
    total_cells = df.shape[0] * df.shape[1]
    total_missing = df.isnull().sum().sum()

    missing_ratio = total_missing / total_cells

    # Scoring logic
    if missing_ratio <= 0.05:
        score = 10
    elif missing_ratio <= 0.10:
        score = 8
    elif missing_ratio <= 0.20:
        score = 6
    elif missing_ratio <= 0.40:
        score = 4
    else:
        score = 2

    warnings = []
    col_missing = df.isnull().mean()

    for col, ratio in col_missing.items():
        if ratio > 0.3:
            warnings.append(f"Column '{col}' has {ratio:.0%} missing values")

    return {
        "score": score,
        "missing_ratio": round(missing_ratio, 3),
        "warnings": warnings
    }
