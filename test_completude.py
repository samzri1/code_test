import pandas as pd

# Load data from source system
source_data = pd.read_csv("source_data.csv")

# Load data from target system
target_data = pd.read_csv("target_data.csv")

# Check if all data from source system is in target system
assert len(source_data) == len(target_data), "Data migration incomplete"