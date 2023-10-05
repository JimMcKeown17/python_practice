import requests
import os
from twilio.rest import Client
account_sid = "ACa3dbc9334a4b64dae110e7b601df5c8f"
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")
number = "+12566394409"

parameters = {
    "q": "Port Elizabeth",
    "appid": api_key,
    "exclude": "current,minutely,daily"

}
url = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour in range(10):
    weather = weather_data['list'][hour]['weather'][0]['id']
    if weather < 700:
        # account_sid = os.environ['TWILIO_ACCOUNT_SID']
        # auth_token = os.environ['TWILIO_AUTH_TOKEN']
        will_rain = True

while will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain!",
        from_='+12566394409',
        to='+27796888002'
    )
    will_rain = False
    print(message.status)

# Download the helper library from https://www.twilio.com/docs/python/install


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
