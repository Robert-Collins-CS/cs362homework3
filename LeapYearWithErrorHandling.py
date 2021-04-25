def checkInput(input_str):
    if input_str.strip().isdigit():
        return True
    else:
        return False


def getUserInp():
    flag = False
    userInp = input("Please input a year number to find out if it is a leap year! \n")
    intInp = 0
    while not flag:
        if checkInput(userInp):
            intInp = int(userInp)
            flag = True
        else:
            userInp = input("Error occured, please enter a to check if then INTEGER year is a leap year! \n")

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
