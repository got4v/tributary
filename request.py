import requests

# Define the URL of your Flask server
url_record = "http://0.0.0.0:8000/record"
url_collect = "http://0.0.0.0:8000/collect"

engine_data = {"engine_temperature": 0.3}

# Make a POST request with the payload data
response_record = requests.post(url_record, json=engine_data)

print("Status connection /record:", response_record.status_code)
print("Content /record:", response_record.text)

# Make a GET request to collect engine temperature
if response_record.status_code == 200:
    response_collect = requests.get(url_collect)
    print("Status connection /collect::", response_collect.status_code)
    print("Content /collect:", response_collect.json())
else:
    print("Failed to get engine temperature data.")
