#The python dictionary deep dive

# profile = {
#     "Phuong": "Im a freelance, computer",
#     "Thanh": "Im a bitch, loser",
#     "Tien": "The biggest dick in the world"
# }
# print(profile["Phuong"])
#
# #adding element
# profile["Nguyen"] = "An asshole!"
# print(profile)
#
# #an empty dictionary
# age = {}
#
# #revalue or edit an item
# profile["Tien"] = "Nothing to do"
# print(profile["Tien"])
#
# #loop dictionary
# for item in profile:
#     print(item)
#     print(profile[item])
#
# student_scores = {
#     "Thanh": 91,
#     "Nam": 50,
#     "Tien": 70,
#     "Dung": 11,
#     "Tung": 89
# }
#
# student_grades = {}
#
# for item in student_scores:
#     student_grades[item] = student_scores[item]
#     if student_grades[item] >= 90:
#         student_grades[item] = "A+"
#     elif student_grades[item] < 90 and student_grades[item] >= 70:
#         student_grades[item] = "A"
#     elif student_grades[item] < 70 and student_grades[item] >= 50:
#         student_grades[item] = "B"
#     else:
#         student_grades[item] = "C"
#
# print(student_grades)
#
#
# #dictionary in dictionary ????
#
# point = {
#     "Day": {
#         "Love": {
#             "Night": "Love all night",
#             "Date": "Simple"
#         },
#         "Not_Love": {
#             "Hate": "Key_Word",
#             "Mad": "Damn"
#         }
#     },
#     "Year": {
#         "I": "for"
#     }
# }
#
# print(point["Day"])
#
# travel_log = {
#     "France":
#         {"City_Visited":
#              ["Paris", "Lille", "Dijon"],
#          "Total_visited": 12
#          },
#     "Germany":
#         {"City_Visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "Total_Visited": 11
#          }
# }
# print(type(travel_log))
#
# travel_log = [
#     {
#         "county": "France",
#         "City_Visited": ["Paris", "Lille", "Dijon"],
#         "Total_visited": 11
#     },
#     {
#         "country": "Germany",
#         "City_Visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "Total_visited": 12
#     },
# ]
#
#
# country = input("Country: ")
# visit = input("Visit: ")
# total = input("Total visit: ")
#
# def add_items(country,visit,total):
#     new_country = {}
#     new_country["country"] = country
#     new_country["visit"] = visit
#     new_country["total"] = total
#     travel_log.append(new_country)
#
# add_items(country, visit, total)
#
# print(f"I had went to {travel_log[2]['country']} {travel_log[2]['total']} times")

