import smtplib
import random
import pandas
import datetime as dt
myEmail = "javapy4@gmail.com"
passwords = "uecxqihxukjmwslm"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=myEmail,password=passwords)
#     connection.sendmail(from_addr=myEmail,
#                         to_addrs="nam783736@gmail.com",
#                         msg="Subject:"
#                         )
#     connection.close()




# datetime module have now , day , month and year

# days = dt.datetime.day
# month = dt.datetime.month
# year = dt.datetime.year
now = dt.datetime.now()
week_day = now.weekday()
# print(week_day)
# -------------------- chalenge ---------------------- #
# if week_day == 3:
#     with open("quotes.txt") as dataFile:
#         content = dataFile.readlines()
#         textlineRand = random.choice(content)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=myEmail, password=passwords)
#         connection.sendmail(from_addr=myEmail,
#                             to_addrs="phuongsepfg@gmail.com",
#                             msg=f"Subject:David \n\n {textlineRand}")
#         connection.close()

# challenge
data = pandas.read_csv("birthdays.csv")
convert = data.to_dict(orient="records")

dict_diff = {data["month"]:data["day"] for (index, data) in data.iterrows()}
fileAfter = ""
file_bd_random = f"IvitationCards/letter{random.randint(1,3)}.txt"

with open(file_bd_random) as datatxt:
    readfile = datatxt.readlines()
    for line in readfile:
        replace = line.replace("[NAME]",convert[0]["name"])
        fileAfter += replace
    for bd in range(0,len(convert)):
        if now.day == convert[bd]["day"] and now.month == convert[bd]["month"]:
            print("correct")
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=myEmail,password=passwords)
                connection.sendmail(from_addr=myEmail,
                                    to_addrs=convert[bd]["email"],
                                    msg=f"Subject:Happy Birthday!\n\n{fileAfter}")
                connection.close()
