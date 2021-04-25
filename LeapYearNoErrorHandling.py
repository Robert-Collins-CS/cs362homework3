def getUserInp():
    userInp = input("Please input a year number to find out if it is a leap year! \n")
    intInp = int(userInp)
    #print(intInp)
    return intInp


def checkLeap(userInput):
    if (userInput % 4) == 0:
        if userInput % 100 == 0 and userInput % 400 != 0:
            print("The year " + str(userInput) + " is NOT a leap year")
            return
        print("The year " + str(userInput) + " is a leap year")
    else:
        print("The year " + str(userInput) + " is NOT a leap year")


checkLeap(getUserInp())
