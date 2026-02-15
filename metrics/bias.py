import pandas as pd
import numpy as np
from scipy.stats import entropy


def bias_score(df: pd.DataFrame, target_column: str):

    warnings = []

    # Check if target column exists
    if target_column not in df.columns:
        return {
            "score": 0,
            "warnings": [f"Target column '{target_column}' not found."],
            "class_distribution": {}
        }

    # Drop missing target rows
    target_data = df[target_column].dropna()

    total = len(target_data)

    if total == 0:
        return {
            "score": 0,
            "warnings": ["Target column has no valid values."],
            "class_distribution": {}
        }

    # Class distribution
    class_counts = target_data.value_counts()
    class_distribution = (class_counts / total).to_dict()

    max_ratio = max(class_distribution.values())

    #Imbalance Check
    if max_ratio > 0.9:
        warnings.append("Severe class imbalance detected (>90%)")
    elif max_ratio > 0.75:
        warnings.append("Moderate class imbalance detected")

    #Entropy Check
    class_probs = list(class_distribution.values())
    ent = entropy(class_probs, base=2)

    max_entropy = np.log2(len(class_probs)) if len(class_probs) > 1 else 0
    normalized_entropy = ent / max_entropy if max_entropy != 0 else 0

    if normalized_entropy < 0.5:
        warnings.append("Low entropy (distribution heavily skewed)")

    #Scoring Logic
    penalty = (1 - normalized_entropy) * 5 + (max_ratio * 3)
    score = max(0, 10 - penalty)
    score = round(score, 2)

    return {
        "score": score,
        "class_distribution": class_distribution,
        "warnings": warnings
    }
