import pandas as pd
from metrics.missing import missing_score

if __name__ == "__main__":
    df = pd.read_csv("sample.csv")
    result = missing_score(df)

    print("\n📊 Missing Value Analysis")
    print("Score:", result["score"])
    print("Missing Ratio:", result["missing_ratio"])

    if result["warnings"]:
        print("Warnings:")
        for w in result["warnings"]:
            print("-", w)
    else:
        print("No major missing value issues detected.")
