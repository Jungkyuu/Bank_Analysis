import pandas as pd

# Load the customer transaction data
df = pd.read_csv("customer_transactions.csv")

# Show the first few rows for reference
print("Preview of transaction data:")
print(df.head())

# Convert transaction_date to datetime and extract the month
df["transaction_date"] = pd.to_datetime(df["transaction_date"])
df["month"] = df["transaction_date"].dt.to_period("M")

# Summarize total amount spent per category
print("\nTotal spending by category:")
category_totals = df.groupby("category")["amount"].sum().sort_values(ascending=False)
print(category_totals)

# Show monthly total spending
print("\nMonthly spending trend:")
monthly_totals = df.groupby("month")["amount"].sum()
print(monthly_totals)

# Detect high-value transactions using 3-sigma rule
mean = df["amount"].mean()
std_dev = df["amount"].std()
threshold = mean + 3 * std_dev

anomalies = df[df["amount"] > threshold]
print(f"\nNumber of unusually high transactions (>{threshold:.2f}): {len(anomalies)}")

# Save these anomalies for manual review
anomalies.to_csv("anomaly_transactions.csv", index=False)
print("Saved high-value transactions to 'anomaly_transactions.csv'")
