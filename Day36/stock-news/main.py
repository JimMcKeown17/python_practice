import requests
import os
import datetime as dt
from twilio.rest import Client

account_sid = "ACa3dbc9334a4b64dae110e7b601df5c8g"
auth_token = "a334f885c2caec85e8360ca3d6349b13"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "1YHFPZZ5XUWAWMJT"
parameters = {
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY",
    "apikey": API_KEY,
    "outputsize": "compact"
}

NEWS_API = "665e90dcf25a4774b93a34984bb8f89g"
NEWS_URL = "https://newsapi.org/v2/everything"

news_parameters = {
    "apiKey": NEWS_API,
    "q": COMPANY_NAME,
    "sortBy": "publishedAt"
}
date = dt.datetime
now = date.now()
yesterday = now - dt.timedelta(days=1)
yesterday = yesterday.strftime('%Y-%m-%d')
day_before = now - dt.timedelta(days=2)
day_before = day_before.strftime('%Y-%m-%d')

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()
yesterday_close = data['Time Series (Daily)'][yesterday]['4. close']
day_before_yesterday = data['Time Series (Daily)'][day_before]['4. close']

percent_change = (float(yesterday_close) - float(day_before_yesterday))/float(day_before_yesterday)
percent_change = 6
# print(yesterday_close, day_before_yesterday)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_response = requests.get(NEWS_URL, params=news_parameters)
news_response.raise_for_status()
news = news_response.json()
article1 = news['articles'][0]['title']
article2 = news['articles'][1]['title']
article3 = news['articles'][2]['title']
article1_desc = news['articles'][0]['description']
article2_desc = news['articles'][1]['description']
article3_desc = news['articles'][2]['description']


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

if abs(percent_change) > 5:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Subject: Tesla Price Moved {percent_change}\n\n"
             f"{article1}"
             f"{article1_desc}",
        from_='+12566394409',
        to='+27796888002'
    )
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

