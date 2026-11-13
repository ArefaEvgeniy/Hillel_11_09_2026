def func(input_list=None):
    if input_list is None:
        input_list = []
    input_list.append(len(input_list))
    return input_list


print(func([4, 6, 0]))
print(func([1, 1]))
print(func())
print(func([1, 2, 7, 0, -1]))
print(func())
print(func())
print(func([1, 7, 90]))
print(func())
