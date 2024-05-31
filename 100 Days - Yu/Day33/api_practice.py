import requests
import datetime as dt
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
#
# iss_position = (latitude, longitude)
#
# print(iss_position)

url = "https://api.sunrise-sunset.org/json"
LAT = 40.579208
LNG = -75.340828
# now = dt.datetime.now()

parameters = {
    "lat": LAT,
    "lng": LNG,
}


response = requests.get(url, params=parameters)
response.raise_for_status()
sunrise = response.json()['results']['sunrise']
sunset = response.json()['results']['sunset']

print(sunrise)