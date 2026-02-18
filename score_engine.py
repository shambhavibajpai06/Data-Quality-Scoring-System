def final_score_engine(missing, redundancy, noise, bias=None):
    """
    Combines all metric scores into one final ML-readiness score.
    Each input must be between 0 and 10.
    """

    # Default weights (you can tweak later)
    weights = {
        "missing": 0.25,
        "redundancy": 0.20,
        "noise": 0.25,
        "bias": 0.30
    }

    # If bias not provided, redistribute weights
    if bias is None:
        weights["missing"] = 0.35
        weights["redundancy"] = 0.30
        weights["noise"] = 0.35

        total_score = (
            missing * weights["missing"] +
            redundancy * weights["redundancy"] +
            noise * weights["noise"]
        )
    else:
        total_score = (
            missing * weights["missing"] +
            redundancy * weights["redundancy"] +
            noise * weights["noise"] +
            bias * weights["bias"]
        )

    total_score = round(total_score, 2)

    # Recommendation logic
    if total_score >= 8:
        recommendation = "High quality dataset. Suitable for production ML."
    elif total_score >= 6:
        recommendation = "Good for experimentation. Moderate production risk."
    elif total_score >= 4:
        recommendation = "Significant issues detected. Cleaning required."
    else:
        recommendation = "Poor dataset quality. Not recommended for ML."

    return {
        "final_score": total_score,
        "recommendation": recommendation
    }
