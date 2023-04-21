import pandas as pd

# Load data from target system
target_data = pd.read_csv("target_data.csv")

# Check if data in target system is consistent with existing data
assert target_data['QuotaAmount'].max() > 1000, "Data inconsistent"
