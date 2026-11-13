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


while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")
    print("6. Option 6")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        option1()

    elif choice == "2":
        option2()

    elif choice == "3":
        option3()

    elif choice == "4":
        option4()

    elif choice == "5":
        option5()

    elif choice == "6":
        option6()

    elif choice == "0":
        print("Exiting the program.")
        break
