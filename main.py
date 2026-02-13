import pandas as pd

from metrics.missing import missing_score
from metrics.redundancy import redundancy_score


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
