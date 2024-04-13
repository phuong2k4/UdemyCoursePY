

print("Welcome to the tip caculator")
total = float(input("What was the total bill\n"))
split = int(input("How many people to split the bill\n"))
tip = int(input("Tip 10 12 or 15\n"))

each_pay = (total / split) * (1+tip/100)

print("Each person u should pay: " + str(each_pay))