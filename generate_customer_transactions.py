import pandas as pd
import numpy as np
import time

# Set a dynamic seed so that data is different every time
np.random.seed(int(time.time()))

# Define the number of records to generate
num_records = 500

# Define possible values for each column
customer_ids = [f"C{str(i).zfill(4)}" for i in range(1, 51)]  # 50 unique customers
transaction_types = ["debit", "credit"]
categories = ["Groceries", "Dining", "Utilities", "Shopping", "Travel", "Rent", "Entertainment"]
regions = ["Ontario", "Quebec", "Alberta", "BC"]
age_groups = ["18-25", "26-35", "36-50", "51+"]

# Generate synthetic data using random choices and distributions
data = {
    "customer_id": np.random.choice(customer_ids, num_records),
    "transaction_date": pd.date_range(start="2023-01-01", periods=num_records, freq="D"),
    "amount": np.round(np.abs(np.random.normal(loc=100, scale=50, size=num_records)), 2),
    "transaction_type": np.random.choice(transaction_types, num_records, p=[0.7, 0.3]),
    "category": np.random.choice(categories, num_records),
    "region": np.random.choice(regions, num_records),
    "age_group": np.random.choice(age_groups, num_records),
}

# Convert the data dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv("customer_transactions.csv", index=False)

# Confirm completion
print("✅ customer_transactions.csv has been successfully created.")
