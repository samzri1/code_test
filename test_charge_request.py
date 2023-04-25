import requests
import time

url = "https://www.google.com"

start_time = time.time()

for i in range(5):
    response = requests.get(url)
    # process the response as needed
    print(f"Request {i+1} completed with status code {response.status_code}")

end_time = time.time()

total_time = end_time - start_time
print(f"Total time taken: {total_time:.2f} seconds")

#python .\test_charge_request.py