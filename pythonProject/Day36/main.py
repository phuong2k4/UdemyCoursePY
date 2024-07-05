import requests
import datetime
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
acount_sid = ""
auth_token = ""

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
api_key_stock = "P7Y1PGRINEEBWTH0"
param_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key_stock,
}
response_stock = requests.get(url="https://www.alphavantage.co/query?",params=param_stock)
response_stock.raise_for_status()
data_stock = response_stock.json()["Time Series (Daily)"]
data_stock_list = [value for (key,value) in data_stock.items()]
# ystd
yesterday_data = data_stock_list[0]
yesterday_close_data = yesterday_data["4. close"]
# before
yesterday_before_data = data_stock_list[1]
yesterday_before_close = yesterday_before_data["4. close"]

diff = abs(float(yesterday_close_data) - float(yesterday_before_close))
percent = (diff / float(yesterday_close_data)) * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
api_key_news = "466e66f1aefe4f8ebc0bdfe46935f7dd"
cpny_name = "tesla"
param_compny = {
    "q": cpny_name,
    "apiKey": api_key_news,
    "cnt": 4,
}
url_api_tsla = "https://newsapi.org/v2/everything?"

response_cpny = requests.get(url=url_api_tsla,params=param_compny)
response_cpny.raise_for_status()
data_cpny = response_cpny.json()

title = data_cpny["articles"][len(data_cpny["articles"])-1]["title"]
content = data_cpny["articles"][len(data_cpny["articles"])-1]["content"]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

up_down = None
if percent <= -5:
    print("Get news")
    up_down = "🔻"
elif percent >= 5:
    print("Get news")
    up_down = "🔺"


client = Client(acount_sid,auth_token)
message = client.messages.create(
    body=f"{STOCK}: {up_down} {percent} \n\nHeadline: {title} \n\nBrief: {content}",
    from_="+number",
    to="+number"
)
print(message.status)


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

