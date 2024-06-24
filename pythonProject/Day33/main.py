import random
import requests
from tkinter import *

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# iss_position = (latitude,longitude)
# print(iss_position)

# --------------------- challenge -------------------- #
# def create_poem():
#     response = requests.get(url="https://api.kanye.rest/")
#     response.raise_for_status()
#     data = response.json()
#     quote = data["quote"]
#     canvas.itemconfig(text,text=quote)
#
# window = Tk()
# window.title("Kanye West says...")
# window.config(padx=30,pady=30,highlightthickness=0, bg="white")
#
# canvas = Canvas(width=300,height=414,highlightthickness=0 ,bg="white")
# background = PhotoImage(file="background.png")
# canvas.create_image(150,200, image=background)
# canvas.grid(column=0,row=0)
#
# text = canvas.create_text(150,190,width=250,text="Kanye Quote",font=("JetBrains Mono",20,"bold"),fill="white")
#
# kanyeImg = PhotoImage(file="kanye.png")
# button = Button(image=kanyeImg, bg="white",command=create_poem)
# button.grid(column=0,row=1)
#
# window.mainloop()


# api sunset and sunrise
# from datetime import datetime
# lat_of_Ny = 40.712776
# long_of_Ny = -74.005974
# param = {
#     "lat": lat_of_Ny,
#     "lng": long_of_Ny,
#     "formatted": 0,
# }
# response = requests.get(url="https://api.sunrise-sunset.org/json",params=param)
# response.raise_for_status()
#
# data = response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
#
# time_now = datetime.now()
# print(time_now.hour)
# print(sunset)
# print(sunrise)

# ------------------ challenge end task ----------------- #
import smtplib
from datetime import datetime

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (latitude,longitude)

lat_of_Ny = 40.712776
long_of_Ny = -74.005974
my_position = (lat_of_Ny,long_of_Ny)

my_email = "javapy4@gmail.com"
anotherEmail = "phuongsepfg@gmail.com"
passwd = "uecxqihxukjmwslm"

def sendmail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=passwd)
        if lat_of_Ny-5 <= float(latitude) <= lat_of_Ny+5 and long_of_Ny-5 <= float(longitude) <= long_of_Ny+5 and darktime():
            print("Done")
            connection.sendmail(from_addr=my_email,
                                to_addrs=anotherEmail,
                                msg="Subject:ISS Space Station\n\n Look up the sky!\n The ISS space station prepare to fly over your location")
        else:
            pass
            print("Wait...")
        connection.close()
def darktime():
    param = {
        "lat": lat_of_Ny,
        "lng": long_of_Ny,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json",params=param)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if sunset <= time_now.hour <= sunrise:
        return True
    else:
        return False
sendmail()
print(iss_position)