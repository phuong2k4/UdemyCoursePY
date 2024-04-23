
#global scope
variable = 5
def acess():
    print(variable)
acess()

#local scope
def entry():
    element = 5
    print(element)
#print(element) // element is not defined

#Modifying global scope

elemt = 123
def modify():
    """Same location in memory"""
        # global elemt
    print(f"{elemt} in local scope. ")
    #or
    return elemt + 1
modify()
print(f"{elemt} in global scope. ")