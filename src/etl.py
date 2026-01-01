import pandas as pd
from dq_issues import run_all_dq_checks

def run_etl():
    df = pd.read_csv("data/raw/provider_specific_file.csv", dtype=str)

    # Strip whitespace from all string columns
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    dq_issues = run_all_dq_checks(df)

    bad_idx = {r["row_index"] for r in dq_issues}
    df_clean = df.drop(index=bad_idx)

    print(f"Loaded: {len(df_clean)}")
    print(f"Failed: {len(bad_idx)}")

    return df_clean, dq_issues