from tkinter import *
import math
# ----------------------- Constants --------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time_loop = None
# ----------------------- TIME RESET --------------------------- #
def reset_time():
    global reps
    reps = 0
    checkmark_label.config(text="")
    window.after_cancel(time_loop)
    canvas.itemconfig(timer_countdown, text ="00:00")
    timer.config(text="Timer")
# ----------------------- TIME MECHANISM --------------------------- #
def button_starting():
    global reps
    reps += 1
    if reps % 8 == 0:
        countDown(LONG_BREAK_MIN * 60)
        timer.config(text="Long Break", fg=GREEN)
    elif reps % 2 == 0:
        countDown(SHORT_BREAK_MIN * 60)
        timer.config(text="Short Break", fg=PINK)

    else:
        countDown(WORK_MIN * 60)
        timer.config(text="WORK", fg=RED)
# ----------------------- COUNTDOWN MECHANISM --------------------------- #

# ----------------------- UI SETUP --------------------------- #

window = Tk()
window.title("Tomato")
window.config(padx=100,pady=100, bg=YELLOW)

def countDown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_countdown, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time_loop
        time_loop = window.after(1000, countDown, count-1)
    else:
        button_starting()
        mark = ""
        for _ in range(0, math.floor(reps/2)):
            mark+="✅"
        checkmark_label.config(text=mark)
# canvas
canvas = Canvas(width=400, height=400,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="ExDay28/tomato.png")
canvas.create_image(200,200,image=tomato_img)
timer_countdown = canvas.create_text(210,190, text="00:00",fill="white",font=(FONT_NAME,45,"bold"))
canvas.grid(column=1,row=1)

# call function


# checkmark
checkmark = "✅"

# label timer
timer = Label(text="Timer" , bg=YELLOW, highlightthickness=0, font=(FONT_NAME,60,"bold"))
timer.grid(column=1, row=0)

# button start
button_start = Button(text="Start",width=10 ,highlightthickness=0, command=button_starting)
button_start.grid(column=0,row=2)

# checkmark
checkmark_label = Label(bg=YELLOW)
checkmark_label.grid(column=1,row=2)

# button reset
button_start = Button(text="Reset", width=10, command=reset_time)
button_start.grid(column=2,row=2)


window.mainloop()