# tkinter module
import tkinter

# window = tkinter.Tk()
# window.title("GUI Tkinter Module")
# window.minsize(width= 500, height= 300)
# window.config(padx=100,pady=100)

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(400,200)
window.config(padx=90,pady=50)
### caculator
# 01-text

def printout():
    convert = int(entry.get()) * 1.609
    km.config(text=convert)

entry = tkinter.Entry(width=10,)
entry.grid(column=3,row=0)

# miles text
label1 = tkinter.Label(text="Miles")
label1.grid(column=4,row=0)

# "is equal to" text
label2 = tkinter.Label(text="is equal to")
label2.grid(column=1,row=2)

# convert km
km = tkinter.Label(text=0)
km.grid(column=3, row=2)

# text km
text_km = tkinter.Label(text="Km")
text_km.grid(column=4,row=2)

# button
button = tkinter.Button(text="Caculate" ,command=printout)
button.grid(column=3,row=3)


window.mainloop()
