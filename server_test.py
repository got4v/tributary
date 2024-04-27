import requests

# Define the URL of your Flask server
url = "http://0.0.0.0:8000/record"

# Define the payload data as a dictionary
payload = {"engine_temperature": 0.3}

# Make a POST request with the payload data
response = requests.post(url, json=payload)

# Print the response status code and content
print("Response Status Code:", response.status_code)
print("Response Content:", response.text)
