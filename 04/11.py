my_list = [6, 55, 0, -100, 33, -12, 0, 89, -22, 11, 44, 55, 66, 77, 88, 99, -56, 98]

result = 0
indexes = []
index = 0
for item in my_list:
    if item > 0:
        result += item
        indexes.append(index)
    index += 1

print("Sum of positive numbers:", result)
print("Indexes of positive numbers:", indexes)


result = 0
indexes = []
for index, value in enumerate(my_list):
    if value > 0:
        result += value
        indexes.append(index)

print("Sum of positive numbers:", result)
print("Indexes of positive numbers:", indexes)
