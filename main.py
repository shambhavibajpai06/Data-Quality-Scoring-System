import pandas as pd
import argparse

from metrics.missing import missing_score
from metrics.redundancy import redundancy_score
from metrics.bias import bias_score


def main():

    parser = argparse.ArgumentParser(
        description="Data Quality Scoring System"
    )

    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to dataset CSV file"
    )

    parser.add_argument(
        "--target",
        type=str,
        required=False,
        help="Target column for bias analysis"
    )

    args = parser.parse_args()

    # Load dataset
    try:
        df = pd.read_csv(args.file)
    except FileNotFoundError:
        print("Dataset file not found.")
        return

    print("\n")
    print("DATA QUALITY ANALYSIS REPORT")

    # Missing Analysis
    print("\n🔎 Missing Value Analysis")
    missing_result = missing_score(df)

    print("Score:", missing_result["score"])
    print("Missing Ratio:", missing_result["missing_ratio"])

    if missing_result["warnings"]:
        for w in missing_result["warnings"]:
            print("-", w)
    else:
        print("No major missing value issues detected.")

    # Redundancy Analysis
    print("\n🔎 Redundancy Analysis")
    red_result = redundancy_score(df)

    print("Score:", red_result["score"])
    print("Duplicate Ratio:", red_result["duplicate_ratio"])

    if red_result["warnings"]:
        for w in red_result["warnings"]:
            print("-", w)
    else:
        print("No major redundancy issues detected.")

    # Bias Analysis (Optional)
    if args.target:
        print("\n Bias Analysis")
        bias_result = bias_score(df, args.target)

        print("Score:", bias_result["score"])

        print("Class Distribution:")
        for cls, ratio in bias_result["class_distribution"].items():
            print(f"  {cls} → {ratio:.2%}")

        if bias_result["warnings"]:
            for w in bias_result["warnings"]:
                print("-", w)
        else:
            print("No major bias issues detected.")
    else:
        print("\n No target column provided. Skipping bias analysis.")

    print("\n")
    print("Analysis Complete")


if __name__ == "__main__":
    main()
