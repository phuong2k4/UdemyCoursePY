import pandas
import random
from tkinter import *
from tkinter import messagebox
import pyperclip
# ------------------------------ constant ----------------------------- #
FONT_NAME = "Courier"

# ------------------------------ system button ----------------------------- #
def button_onclick():

    user_confirm = messagebox.askokcancel(title="Confirm Infomation", message=f"Confirm: \nEmail:{textEmail.get()}\nPassword: {textPassword.get()}")
    if textWebsite.get() == "" or textPassword == "":
        messagebox.showerror(title="Error Empty", message="Name website or password is empty.\nPlease fill all the field to continue!")
    elif user_confirm:
        with open("ExDay29/data.txt","a") as data:
            data.write(f"{textWebsite.get()} | {textEmail.get()} | {textPassword.get()}\n")
            data.close()
            textWebsite.delete(0,END)
            textPassword.delete(0,END)

# ------------------------------ system generate ----------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

randLetter = random.randint(8,10)
randNumber = random.randint(2,4)
randsymbol = random.randint(2,4)

gene_letter = [random.choice(letters) for _ in range(randLetter)]
gene_symbol = [random.choice(symbols) for _ in range(randsymbol)]
gene_number = [random.choice(numbers) for _ in range(randNumber)]
password_convert = gene_letter + gene_number + gene_symbol

def generator_pass():
    textPassword.insert(0,"".join(password_convert))
    pyperclip.copy("".join(password_convert))


# ------------------------------ system ui----------------------------- #

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
textWebsite.focus()
textWebsite.grid(column=1,row=1,columnspan=2)

textEmail = Entry(width=36)
textEmail.insert(1,"google.com")
textEmail.grid(column=1,row=2,columnspan=2)

textPassword = Entry(width=24)
textPassword.grid(column=1,row=3)

button_generate = Button(text="Cre PassW", bg="white",highlightthickness=0, command=generator_pass)
button_generate.grid(column=2,row=3)

button_add = Button(width=34,text="Add", bg="white",highlightthickness=0, command=button_onclick)
button_add.grid(column=1,row=4,columnspan=2)
window.mainloop()

# ------------------------------ system button ----------------------------- #





