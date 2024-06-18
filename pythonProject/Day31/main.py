import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
currentCard = {}


# ui setup
window = Tk()
window.title("Flash")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


# read file
try:
    data = pandas.read_csv("word_learn.csv")
    convert = data.to_dict(orient="records")
except:
    data = pandas.read_csv("language.csv")
    convert = data.to_dict(orient="records")

# function


def changeCard():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_text, text=currentCard["english"],fill="white")
    canvas.itemconfig(card_backgr, image=card_back)
def next():
    global currentCard,flip_time
    window.after_cancel(flip_time)
    currentCard = random.choice(convert)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_text, text=currentCard["french"],fill="black")
    canvas.itemconfig(card_backgr,image=card_front)
    flip_time=window.after(3000, func=changeCard)

def is_know():
    convert.remove(currentCard)
    data_know = pandas.DataFrame(convert)
    data_know.to_csv("work_learn.csv", index=False)
    next()

flip_time = window.after(3000, func=changeCard)
# img ui
canvas = Canvas(width=800, height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
# img back
card_back = PhotoImage(file="img/card_back.png")
# img front
card_front = PhotoImage(file="img/card_front.png")
card_backgr= canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)


# text UI
card_title=canvas.create_text(400,63,text="", font=("JetBrains Mono",40, "bold"))
card_text=canvas.create_text(400,263,text="" , font=("JetBrains Mono",30, "bold"))
# button UI
wrongPng = PhotoImage(file="img/wrong.png")
wrongButton = Button(image=wrongPng,command=next)
wrongButton.grid(column=0,row=1)
# wrongButton.place(x=300,y=750)

rightPng = PhotoImage(file="img/right.png")
rightButton = Button(image=rightPng,command=is_know)
# rightButton.place(x=800,y=750)
rightButton.grid(column=1,row=1)

next()
window.mainloop()

