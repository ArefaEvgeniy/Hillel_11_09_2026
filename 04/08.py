while True:
    age = input("Enter your age: ")
    if age.isdigit():
        break
    print("Invalid input. Please enter a valid age.")

print("Your age is:", age)
