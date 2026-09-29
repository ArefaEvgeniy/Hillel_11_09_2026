my_list = [6, 55, 0, -100, 33, 12, 10, 89, 22, 11, 44, 55, 66, 77, 88, 99, 56, 98]

result = 0
for item in my_list:
    if item % 11 == 0:
        continue

    if item > 0:
        result += item

    if result > 200:
        break
else:
    print("Loop has ended.")

print("Sum 2 of positive numbers:", result)
