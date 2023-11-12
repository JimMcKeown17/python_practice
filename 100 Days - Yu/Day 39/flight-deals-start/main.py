from datetime import datetime as dt
import requests

sheety_url = "https://api.sheety.co/55b89bfbfd63b45f11e9bd1c7f988e16/flightDeals/prices"
response = requests.get(sheety_url)
response.raise_for_status()
data = response.json()
print(data)


# Sample data to post
new_data = {
    "prices": {
        "city": "Sample City",
        "iataCode": "SCY",
        "lowestPrice": 999,
    }
}

headers = {
    "content-type": "application/json"
}

# Making the POST request to add the new data
response = requests.post(sheety_url, json=new_data, headers=headers)

# Raise an exception for any HTTP errors
response.raise_for_status()
print(response.text)
