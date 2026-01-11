# 🏥 CMS Provider Data Quality Pipeline

This project builds a scalable, rule-driven pipeline for validating and analyzing **CMS provider-specific data**. It combines Python and SQL to ingest raw files, apply data quality (DQ) rules, log ETL activity, and generate audit-ready summaries and issue reports. The framework is modular, extensible, and designed for automation and stewardship.

---

## 🎯 Project Goals

- Ingest and validate CMS provider files
- Apply standardized DQ rules across key fields
- Log ETL and DQ execution metadata
- Generate rule summaries and row-level failure details
- Support automation and scheduled DQ runs
- Enable stewardship via comment tracking and profiling

---



---

## 🧪 Data Quality Framework

Each rule is defined with:

- `rule_id`, `field_name`, `rule_name`, `rule_description`
- SQL logic with `{run_id}` and `{rule_id}` placeholders
- Severity level and activation flag

### Key Tables

| Table                  | Purpose                                      |
|------------------------|----------------------------------------------|
| `dq_rules`             | Rule metadata and SQL logic                  |
| `dq_rule_summary`      | Rule-level failure counts                    |
| `dq_results`           | Row-level failure details                    |
| `dq_issues`            | Python-based issue tracking                  |
| `etl_log`              | ETL run metadata                             |

---

## ⚙️ Execution Flow

1. Create database: `CMS_PDS_DATA`
2. Run all table scripts from `sql/`
3. Place raw CSV in `data/raw/`
4. Run `main_code.ipynb` to trigger ETL and DQ
5. Python DQ rules log to `dq_issues`
6. SQL DQ rules run via `run_dq_rules` stored procedure
7. Results populate `dq_rule_summary` and `dq_results`
8. Add comments using `Data Steward Comment_High_invalid.txt`

---

## 🗓️ Automation

To schedule DQ execution:

- Refer to `dq rule schedule setting_Automation_running Dq rules.txt`
- Use SQL Agent or Python scheduler to run `run_dq_rules` at defined intervals

---

## 🧠 Getting Started

```bash
# Step 1: Create database
Run CMS_PDS_DATA creation in SSMS

# Step 2: Create tables
Run all .sql files in /sql

# Step 3: Load rules
Run main_code.ipynb to insert rules from Clean_DQ_Rules.xlsx

# Step 4: Run ETL + DQ
Run main_code.ipynb to load data and apply rules

