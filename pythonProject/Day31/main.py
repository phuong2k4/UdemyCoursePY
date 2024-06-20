import random
from tkinter import *
import pandas

randomCard = {}
BACKGROUND_COLOR = "#B1DDC6"
# read file
try:
    data = pandas.read_csv("data_know.csv")
    convert = data.to_dict(orient="records")
except:
    data = pandas.read_csv("language.csv")
    convert = data.to_dict(orient="records")
# button
def changeCard():
    canvas.itemconfig(card,image=card_back)
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_content,text=randomCard["english"],fill="white")

def next_card():
    global randomCard,flip
    window.after_cancel(flip)
    randomCard = random.choice(convert)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_content,text=randomCard["french"],fill="black")
    flip = window.after(3000,func=changeCard)


def know_card():
    convert.remove(randomCard)
    card_know = pandas.DataFrame(convert)
    card_know.to_csv("data_know.csv")
    next_card()
# ui setup
window = Tk()
window.title("Flash")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip = window.after(3000,func=changeCard)
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_back = PhotoImage(file="img/card_back.png")
card_front = PhotoImage(file="img/card_front.png")
card = canvas.create_image(400,263,image=card_front)
canvas.grid(column=0,row=0,columnspan=2)

# text
card_title = canvas.create_text(400,63,text="", font=("JetBrains Mono",45,"bold"))
card_content = canvas.create_text(400,263,text="", font=("JetBrains Mono",30,"bold"))

know_button = PhotoImage(file= "img/right.png")
button_know = Button(image=know_button,command=know_card)
button_know.grid(column=1,row=1)

dknow_button = PhotoImage(file="img/wrong.png")
button_dknow = Button(image=dknow_button,command=next_card)
button_dknow.grid(column=0,row=1)

next_card()
window.mainloop()

