import requests
import datetime
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
api_key_stock = "41SMB8TVN6K2MRJ8"
param_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key_stock,
}
response_stock = requests.get(url="https://www.alphavantage.co/query?",params=param_stock)
response_stock.raise_for_status()
data_stock = response_stock.json()
print(data_stock)
# data_stock_list = [value for (key,value) in data_stock.items()]
# for value in data_stock_list:
#     print(value)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# api_key_news = "466e66f1aefe4f8ebc0bdfe46935f7dd"
# cpny_name = "tesla"
# param_compny = {
#     "q": cpny_name,
#     "apiKey": api_key_news,
#     "cnt": 4,
# }
# url_api_tsla = "https://newsapi.org/v2/everything?"
#
# response_cpny = requests.get(url=url_api_tsla,params=param_compny)
# response_cpny.raise_for_status()
# data_cpny = response_cpny.json()
# print(data_cpny)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

# acount_sid = "ACd99e0cb0a49bbdf7db6ade94c0d6943b"
# auth_token = "a1077124dda7f89fc1a2088510154ae8"
# client = Client(acount_sid,auth_token)
# message = client.messages.create(
#     body="//",
#     from_="+16283454367",
#     to="+84964032988"
# )

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

