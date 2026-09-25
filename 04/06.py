first_list = [2, 4, 7, 11, 0, -2, 8]
a = [False, 0, None, [], '']
print(min(first_list))
print(max(first_list))

second_list = ['2', '4', 'a', 'Hello', 'z', 'A']
print(min(second_list))
print(max(second_list))

print(all(first_list))
print(all(second_list))

print(any(first_list))
print(any(second_list))
print(any(a))

print(list(reversed(first_list)))
print(first_list)

first_list.reverse()
print(first_list)
