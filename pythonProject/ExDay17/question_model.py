class Question:
    def __init__(self, text, answer):
        self.iText = text
        self.Ianswer = answer


class QuizzBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.list = question_list

    def quizz(self):

        current_question = self.list[self.question_number]
        self.question_number += 1
        ans = input(f"Q:{self.question_number}: {current_question.iText}. True or False? : ")
        if ans == current_question.Ianswer:
            self.score += 1
            print("You got it right. ")
            print(f"The correct answer is {current_question.Ianswer}")
            print(f"SCORE: {self.score}")
            return True
        else:
            print(f"Final score: {self.score}")
            return f"Correct answer is {current_question.Ianswer}. U wrong!"

    def still_has_question(self):
        if self.question_number < len(self.list):
            return True
        else:
            return False



