# sending message using twilio api send mess
import os
from twilio.rest import Client

API_SID = ""
AUTH_TOKEN = ""
FROM_PHONE = "+16283454367"
TO_PHONE = "+840964032988"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(API_SID, AUTH_TOKEN)
    def sendMessage(self):
        self.message = self.client.messages.create(
            body=f"Low price alert!!! Only to fly from  to, from to .",
            from_= FROM_PHONE,
            to= TO_PHONE
        )
        print(self.message.status)
    pass
