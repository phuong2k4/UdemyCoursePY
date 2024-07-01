import requests

api = "11374b8f31ace43e25495e595b7e0513"

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
# data2 = data["list"][0]["weather"]
# print(data2)
# print(data["list"][0]["weather"][0]["id"])
for index in data["list"]:
    condition = index["weather"][0]["id"]
    if int(condition) < 700:
        print("Bring umbrella back")