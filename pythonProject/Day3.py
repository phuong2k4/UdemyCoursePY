sizeS = 15
sizeM = 20
sizeL = 25
print("Thanks for choosing Python Pizza Deliver")
size = str(input("What size pizza do you want?"))
add_pepperoni = str(input("Do you want pepperoni? Yes or No?"))
add_extra_cheese = str(input("Wanna extra cheese? Brother?"))
if add_pepperoni == "Y":
    if(size == "S"):
        sizeS +=2
    elif(size == "M"):
        sizeM +=3
    elif(size == "L"):
        sizeL +=3
if add_extra_cheese == "Y":
    sizeS += 1
    sizeM += 1
    sizeL += 1
if size == "S":
    print("The final bill is: " + str(sizeS))
if size == "M":
    print("The final bill is: " + str(sizeM))
if size == "L":
    print("The final bill is: " + str(sizeL))
