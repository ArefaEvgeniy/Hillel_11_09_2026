def option1():
    print("You selected Option 1")


def option2():
    print("You selected Option 2")


def option3():
    print("You selected Option 2")


def option4():
    print("You selected Option 4")


def option5():
    print("You selected Option 5")


def option6():
    print("You selected Option 6")


def option0():
    print("Exiting the program.")


def wrong():
    print("Invalid choice. Please try again.")


choices = {
    "1": option1,
    "2": option2,
    "3": option3,
    "4": option4,
    "5": option5,
    "6": option6,
    "0": option0
}

while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")
    print("6. Option 6")
    print("0. Exit")

    choice = input("Enter your choice: ")

    choices.get(choice, wrong)()

    if choice == "0":
        break
