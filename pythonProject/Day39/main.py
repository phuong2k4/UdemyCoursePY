#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from notification_manager import NotificationManager
from data_manager import DataManager

datamanager = DataManager()
datamanager.data()

send = NotificationManager()
send.sendMessage()
