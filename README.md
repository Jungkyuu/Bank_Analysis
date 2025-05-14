# Bank Transaction Data Analysis

This is a personal project where I looked into a set of sample bank transactions to better understand customer spending habits. I used Python and Excel to break down spending by category, find trends over time, and spot anything that looked unusual (like really large transactions).

## 📁 What’s Included

- `generate_customer_transactions.py`  
  Creates a CSV file (`customer_transactions.csv`) with 500 rows of randomly generated transactions.  
  Each row includes customer ID, date, amount, category, region, and more.

- `csv_to_excel_converter.py`  
  Converts the CSV file into an Excel file (`customer_transactions.xlsx`).  
  Useful for working in Excel or importing into visualization/reporting tools.

## Things I Looked Into

- Which categories customers spend the most on
- Monthly changes in total spending
- Transactions that might be outliers

## 🛠 Tools I Used

- Python (pandas for data creation and processing)
- Excel (for tabular summaries and basic charts)
- Power BI (web version used to build an interactive report from the CSV)

## 📊 Power BI Visualization

This project includes a Power BI report created using data generated from `customer_transactions.csv`.

Since the data is generated randomly each time the Python script is run,  
**the visualization below represents one specific run of the data generation script.**

The dashboard shows the total transaction amounts by category, based on customer spending records.

### 🔍 Visualization Snapshot

<img width="1064" alt="Screenshot 2025-05-14 at 6 55 46 PM" src="https://github.com/user-attachments/assets/1492ed98-508f-49ca-94a5-84dc1813baa1" />


> Built using [Power BI Online](https://app.powerbi.com) on macOS  
> Screenshot taken from one version of the generated data

## ▶️ How to Run This

1. Make sure you have Python and `pandas` installed.
2. Then run each script one by one in the following order:

```bash
# Step 1: Generate random transaction data
python3 generate_customer_transactions.py

# Step 2: Convert the CSV to Excel format
python3 csv_to_excel_converter.py

# Step 3: Analyze the data and detect anomalies
python3 bank_analysis.py
