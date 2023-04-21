import pandas as pd
import time as time
import pytest as pytest

# Load data from target system
target_data = pd.read_csv("target_data.csv")

# Measure time to perform operation on data
start_time = time.time()
operation_result = target_data.groupby('QuotaAmount').sum()
end_time = time.time()

# Check if operation took less than 1 second
assert end_time - start_time < 1, "Performance unacceptable"
