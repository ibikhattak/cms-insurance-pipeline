# Bank of America Financial Statements Pipeline

This project builds an end-to-end pipeline for analyzing Bank of America's financial statements over the past five years. It collects income statements and balance sheets, cleans and standardizes the data, applies data quality checks, computes key financial ratios, and visualizes trends over time.

## Project Goals
- Download Bank of America's financial statements (5-year period)
- Clean and standardize the data
- Apply data quality checks (DQ rules)
- Compute key financial ratios (ROA, ROE, efficiency ratio, loan-to-deposit)
- Visualize trends and insights

## Folder Structure

## Data Sources
- Yahoo Finance (yfinance)
- SEC EDGAR (optional future expansion)

## Key Ratios
- Return on Assets (ROA)
- Return on Equity (ROE)
- Efficiency Ratio
- Loan-to-Deposit Ratio

## Getting Started
Install dependencies:

Run the pipeline modules inside the `src/` directory or explore the notebooks in `notebooks/`.

## Future Enhancements
- Add cash flow statement
- Add Basel III capital ratios
- Add CCAR-style stress testing
