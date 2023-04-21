import pandas as pd

# Load data from target system
target_data = pd.read_csv("target_data.csv")

# Check if data in target system meets company requirements
assert target_data['QuotaAmount'].dtype == 'int64', "Data type incorrect"


#float64