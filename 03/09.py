age = input("Please enter your age: ")

if not age.isdigit() or int(age) <= 0:
    print("Invalid input. Please enter a valid age.")
elif int(age) < 10:
    print("Milk")
elif int(age) < 18:
    print("Juice")
elif int(age) <= 70:
    print("Beer")
elif int(age) < 100:
    print("Tea")
else:
    print("Invalid age range. Please enter an age between 1 and 99.")
