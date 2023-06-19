import requests
import json

def make_rest_call(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        print(json.dumps(json_data, indent=4))
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Example REST endpoint URL
endpoint_url = "https://api.github.com/users/siddharthborah"

# Make the REST call
make_rest_call(endpoint_url)