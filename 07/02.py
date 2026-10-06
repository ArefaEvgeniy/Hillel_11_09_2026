input_list = [5, 1, 2, 0, 3, 1, 4, 45, 50, 3, 2, 1, 0, 5, 4, 0, 50, 5, 3, 1, 2, 0]

new_list = []
for i in input_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)

new_list_2 = list(set(new_list))
print(new_list_2)
