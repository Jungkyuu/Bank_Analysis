import pandas as pd

# Load the existing CSV file
csv_file = "customer_transactions.csv"
df = pd.read_csv(csv_file)

# Save it as an Excel file
excel_file = "customer_transactions.xlsx"
df.to_excel(excel_file, index=False)

print(f"✅ Excel file '{excel_file}' has been created from '{csv_file}'.")
