number = int(input("Enter a number: "))

result = 0
while number > 0:
    print("Current number:", number)
    if number % 5 == 0:
        print("Number is divisible by 5. Skipping this iteration.")
        number -= 1
        continue
    result += number  # result = result + number
    if result >= 1000:
        print("Result has reached or exceeded 1000. Breaking the loop.")
        break
    number -= 1
else:
    print("Loop has ended.")

print("Sum of numbers:", result)
