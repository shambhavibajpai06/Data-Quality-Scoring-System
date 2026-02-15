import pandas as pd

from metrics.missing import missing_score
from metrics.redundancy import redundancy_score
from metrics.bias import bias_score


if __name__ == "__main__":

    # Load dataset
    df = pd.read_csv("sample.csv")

    print("DATA QUALITY ANALYSIS REPORT")

   
    #Missing Value Analysis
    
    print("\n🔎 Missing Value Analysis")
    missing_result = missing_score(df)

    print("Score:", missing_result["score"])
    print("Missing Ratio:", missing_result["missing_ratio"])

    if missing_result["warnings"]:
        for w in missing_result["warnings"]:
            print("-", w)
    else:
        print("No major missing value issues detected.")


    #Redundancy Analysis
    print("\n🔎 Redundancy Analysis")
    red_result = redundancy_score(df)

    print("Score:", red_result["score"])
    print("Duplicate Ratio:", red_result["duplicate_ratio"])

    if red_result["warnings"]:
        for w in red_result["warnings"]:
            print("-", w)
    else:
        print("No major redundancy issues detected.")

    print("Analysis Complete")

    #Bias Analysis
    
    print("\n🔎 Bias Analysis")

    # Change this to your actual target column name
    bias_result = bias_score(df, target_column="department")

    print("Score:", bias_result["score"])
    print("Class Distribution:")

    for cls, ratio in bias_result["class_distribution"].items():
        print(f"  {cls} → {ratio:.2%}")

    if bias_result["warnings"]:
        for w in bias_result["warnings"]:
            print("-", w)
    else:
        print("No major bias issues detected.")

