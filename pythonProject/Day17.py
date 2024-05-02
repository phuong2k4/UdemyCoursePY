#class and create class in Python

# class Car:
#     def __init__(self, id_car, name_car):
#         self.id = id_car
#         self.name = name_car
#     def speed_car(self, kmh):
#         print(kmh)
#
#
# BMW_Car = Car(123, "BMW")
#
# print(BMW_Car.speed_car(190))

from ExDay17.question import question_data
from ExDay17.question_model import Question

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
print(question_bank[0].Ianswer)

