from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizzInterface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


# name: str
# age: int
# gpa: float
# is_human: bool
#
# def checkHuman(is_human: bool):
#     if is_human:
#         print("U are verify")
#     else:
#         print("U not a human")
#
# def password(name: str) -> bool: # -> is return datatype
#     if name:
#         return True
#     else:
#         return False
#
# name = input("Your name: ")
# checkHuman(password(name))