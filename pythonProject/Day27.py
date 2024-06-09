# tkinter module
import tkinter

window = tkinter.Tk()
window.title("GUI Tkinter Module")
window.minsize(width= 500, height= 300)

# Label
my_label = tkinter.Label(text="I am a free lance", font=("JetBrains Mono", 24, "bold"))
my_label.pack() # change label position





window.mainloop()
