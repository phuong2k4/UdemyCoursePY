# -------------- Constants ------------- #
FONT_NAME = "Courier"

# -------------- UI Setup ---------------#
from tkinter import *
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="white")

canvas = Canvas(width=200,height=200,highlightthickness=0,bg="white")
imageLock = PhotoImage(file="ExDay29/lock.png")
canvas.create_image(100,100,image=imageLock)
canvas.grid(column=1,row=0)

labelWebsite = Label(text="Website:" ,font=(FONT_NAME,10), bg="white")
labelWebsite.grid(column=0,row=1)

labelWebsite = Label(text="Email/Username:" ,font=(FONT_NAME,10), bg="white")
labelWebsite.grid(column=0,row=2)

labelWebsite = Label(text="PassWord:" ,font=(FONT_NAME,10), bg="white")
labelWebsite.grid(column=0,row=3,)

textWebsite = Entry(width=36)
textWebsite.grid(column=1,row=1,columnspan=2)

textEmail = Entry(width=36)
textEmail.grid(column=1,row=2,columnspan=2)

textPassword = Entry(width=24)
textPassword.grid(column=1,row=3)

button_generate = Button(text="Cre PassW", bg="white",highlightthickness=0)
button_generate.grid(column=2,row=3)

button_add = Button(width=34,text="Add", bg="white",highlightthickness=0)
button_add.grid(column=1,row=4,columnspan=2)
window.mainloop()
