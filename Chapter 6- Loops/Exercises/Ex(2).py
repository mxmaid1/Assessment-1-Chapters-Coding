print("Enter age please")
while True:
    inputting=input("Input: ")
    if inputting=="quit":
        break
    else:
        age=int(inputting)
        if age < 3:
            print("The ticket is free!\n")
        elif 3 <= age <= 12:
            print("The ticket costs $10.\n")
        else:
            print("The ticket costs $15.\n")