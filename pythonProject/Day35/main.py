import requests
import os
from twilio.rest import Client
from datetime import datetime
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("SID_ACCOUNT")
auth_token = os.environ.get("AUTH_TOKEN")
api = os.environ.get("API_KEY")
param = {
    "lat": 21.027763,
    "lon": 105.834160,
    "appid": api,
    "cnt": 4,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=param)
response.raise_for_status()
print(response)

data = response.json()
datetime = datetime.now()

# if datetime == data["list"][0]["dt_txt"]:
#     print("Its time")
# else:
#     print("Wait")

for index in data["list"]:
    condition = index["weather"][0]["id"]
    if int(condition) < 700 and datetime == index["dt_txt"]:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Hello David.\nIts rain today, in {index['dt_txt']}, bring an umbrella\nSMS Send by Python api",
            from_="apinumber",
            to="unumber",
        )
        print(message.status)