import tkinter
window = tkinter.Tk()
window.title("GUI tkinter module")
window.minsize(500,500)

# unlimited argument (using * + name_Argument)

# def add(*args):
#     tong = 0
#     for n in args:
#         tong += n
#     print(tong)
# add(1,2,3,4,5)

# def profile(intro, **information):
#     # type = dictionary
#     # print(type(information))
#     # for key,value in information.items():
#     #     print(key)
#     #     print(value)
#     intro += information["point"]
#     print(intro)
#
# profile(3, name="david", age="21",point= 66,)

class Human:
    def __init__(self, **kw):
        self.name = kw.get("name")
        self.age = kw.get("age")

new_human = Human(nam= "jones", age= 23)
print(new_human.name)
print(new_human.age)

# Label
my_label = tkinter.Label(text="I am a free lance", font=("JetBrains Mono", 24, "bold"))
my_label.pack() # change label position
my_label["text"] = "New Text"
my_label.config(text= "New Text") # change defaul text label

# Button
def button_onclick():
    my_label.config(text=input.get())
button = tkinter.Button(text="Click me", command= button_onclick)
button.pack()


# entry
input = tkinter.Entry(width=10)
input.pack()
input.insert(1, "text something")
print(input.get())

# text
text = tkinter.Text(width=20, height=5)
# cursor in textbox
text.focus()
text.pack()
# add some text
# text.insert(2,"Muti-line text entry")

# spin box
def printout_spinbox():
    print(int(spin_box.get()) + 1)
spin_box = tkinter.Spinbox(from_=0 , to= 100, width=5, command=printout_spinbox)
spin_box.pack()

# scale
def printout_scale():
    t = scale.get()
    text.insert(0,t)
scale = tkinter.Scale(from_=0, to= 1000, width=20, command=printout_scale)
scale.pack()

# check button
def if_check():
    change = ["On"]
    check_button.config(text= change)
check_state = 0
check_button = tkinter.Checkbutton(text="is on?", variable=check_state, command= if_check)
check_button.pack()

# radio_button
radio_button1 = tkinter.Radiobutton(text="option1", value=1)
radio_button1.pack()
radio_button2 = tkinter.Radiobutton(text="option2" , value=2)
radio_button2.pack()

# listbox
def cursor():
    list_box.curselection()

list_box = tkinter.Listbox( height=4)
fruits = ["apple", "mango", "dragon_fruit", "orange"]
for fruit in fruits:
    list_box.insert(fruits.index(fruit), fruit)
list_box.bind("<<ListBoxSelect>>", cursor)
list_box.pack()



# challege 011
# # Label
# my_label = tkinter.Label(text="I am a free lance", font=("JetBrains Mono", 24, "bold"))
# my_label.grid(column= 0, row=0) # change label position
# my_label["text"] = "New Text"
# my_label.config(text= "New Text") # change defaul text label
#
# # Button
# def button_onclick():
#     my_label.config(text=input.get())
# button = tkinter.Button(text="Click me", command= button_onclick)
# button.grid(column=1, row=1)
# button.config(padx=10, pady=10)
#
# # entry
# input = tkinter.Entry(width=10)
# # input.place(x=0, y=0)
# input.grid(column=2,row=3)
# input.insert(1, "text something")
# print(input.get())
#
# button2= tkinter.Button()
# button2.grid(column=2, row= 0)

window.mainloop()