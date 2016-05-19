"""
    Control flow gives us this ablity to choose amoung
    outcomes based off what else is happening in the program
"""


def clinic():
    print("You have entered the clinic!")
    print("Do you take the door on the left or the right?")
    answer = input("Type Left or Right and Hit Enter").lower()
    print(answer)
    if answer == "left" or answer == "l":
        print("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
        print("Of course this is the V Room,I've told you that already!")
    else:
        print("You did'nt pick left or right! Try Again")
        clinic()

clinic()
