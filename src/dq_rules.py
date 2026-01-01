import pandas as pd
import re

REQUIRED_FIELDS = [
    "providerCcn", "effectiveDate", "stateCode", "providerType",
    "fiscalYearBeginDate", "fiscalYearEndDate", "exportDate", "lastUpdated"
]

DATE_FIELDS = [
    "effectiveDate", "fiscalYearBeginDate", "fiscalYearEndDate",
    "exportDate", "terminationDate", "lastUpdated"
]

NUMERIC_FIELDS = [
    "operatingCostToChargeRatio", "capitalCostToChargeRatio",
    "specialProviderUpdateFactor", "supplementalSecurityIncomeRatio",
    "medicaidRatio", "uncompensatedCareAmount"
]

def issue(col, msg, row, idx):
    return {
        "row_index": idx,
        "issue_column": col,
        "issue_message": msg,
        "row_data": row.to_dict()
    }

def is_missing(val):
    return val is None or pd.isna(val) or (isinstance(val, str) and val.strip() == "")

def is_valid_yyyymmdd(val):
    if is_missing(val):
        return True
    return isinstance(val, str) and bool(re.fullmatch(r"\d{8}", val))

def is_valid_numeric(val):
    if is_missing(val):
        return True
    try:
        float(val)
        return True
    except:
        return False

def check_completeness(df):
    issues = []
    for i, row in df.iterrows():
        for col in REQUIRED_FIELDS:
            if is_missing(row.get(col)):
                issues.append(issue(col, "Missing required value", row, i))
    return issues

def check_validity(df):
    issues = []
    for i, row in df.iterrows():
        cc = row.get("providerCcn")
        if not is_missing(cc) and not (str(cc).isdigit() and len(str(cc)) == 6):
            issues.append(issue("providerCcn", "Must be 6-digit numeric", row, i))

        sc = row.get("stateCode")
        if not is_missing(sc) and not (str(sc).isdigit() and len(str(sc)) == 2):
            issues.append(issue("stateCode", "Must be 2-digit numeric", row, i))

        pt = row.get("providerType")
        if not is_missing(pt) and not str(pt).isdigit():
            issues.append(issue("providerType", "Must be numeric", row, i))

        for col in DATE_FIELDS:
            if not is_valid_yyyymmdd(row.get(col)):
                issues.append(issue(col, "Invalid YYYYMMDD format", row, i))

        for col in NUMERIC_FIELDS:
            if not is_valid_numeric(row.get(col)):
                issues.append(issue(col, "Invalid numeric value", row, i))

    return issues

def check_uniqueness(df):
    issues = []
    dup = df[df.duplicated(
        ["providerCcn", "effectiveDate", "nationalProviderIdentifier"],
        keep=False
    )]
    for i, row in dup.iterrows():
        issues.append(issue(
            "providerCcn",
            "Duplicate providerCcn + effectiveDate + NPI",
            row,
            i
        ))
    return issues

def run_all_dq_checks(df):
    return (
        check_completeness(df)
        + check_validity(df)
        + check_uniqueness(df)
    )