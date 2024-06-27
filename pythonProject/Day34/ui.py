THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizzInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=350, height=250, bg="white")
        self.question = self.canvas.create_text(150,125,width=250,text="Something in here",fill=THEME_COLOR,font=("Arial",15,"italic"))
        self.canvas.grid(column= 0,row=1,columnspan = 2,pady=50)

        self.label = Label(text="Score: 0",highlightthickness=0,bg=THEME_COLOR,font="white")
        self.label.grid(column= 1,row =0)

        trueimg = PhotoImage(file="images/true.png")
        self.true = Button(image=trueimg,command=self.trueF)
        self.true.grid(column= 0, row=2)

        falseimg = PhotoImage(file="images/false.png")
        self.false = Button(image=falseimg,command=self.falseF)
        self.false.grid(column=1, row=2)


        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text="You done!")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def trueF(self):
        self.canvas.config(bg="white")
        self.get_ans(self.quiz.check_answer("true"))


    def falseF(self):
        self.get_ans(self.quiz.check_answer("false"))

    def get_ans(self,check):
        if check:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(100, self.get_next_question)
