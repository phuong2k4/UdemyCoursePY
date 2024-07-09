import requests
import json
from datetime import datetime

# authorize
app_ID = "94d6c2ed"
app_Key = "24da69d255eb9b934aac2ec9c1af40da"

# url use sheet
URL_sheet = "https://api.sheety.co/73d4550fa5122eb2b6e85ac737d5c7a0/workourTracking/trangTính1"

GENDER = "MAN"
WEIGHT_KG = 51
HEIGHT_CM = 170
AGE = 21

user = input("Tell which exercises you did: ")

body = {
   "query": user,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response_track_api = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise", headers={
    "Content-Type": "application/json",
        "x-app-id": app_ID,
        "x-app-key": app_Key,
    },
    json=body
)

data = response_track_api.json()

# authentication

response_sheety_get = requests.get(url=URL_sheet)
print(response_sheety_get.status_code)
date = datetime.now()
for value in data["exercises"]:
    add_value = {
        "trangTính1": {
          "date": date.strftime("%d/%m/%Y"),
          "time": date.strftime("%H:%M:%S"),
          "exercise": value["user_input"],
          "duration": value["duration_min"],
          "calories": value["nf_calories"],
        }
    }
    response_sheety_add = requests.post(url=URL_sheet, json=add_value)
    print(response_sheety_add.status_code)