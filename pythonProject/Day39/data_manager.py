# use sheety.co to struct all data flight price
import requests
url_sheet = "https://api.sheety.co/73d4550fa5122eb2b6e85ac737d5c7a0/flight/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(url=url_sheet)
    def data(self):
        datasheet = self.response.json()
        for rows in datasheet["prices"]:
            print(rows)
    pass