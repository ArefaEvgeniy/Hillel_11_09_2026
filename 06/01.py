a = [1, 45, "tt", [1, 2, 3], 4.5]
b = (1, 45, "tt", [1, 2, 3], 4.5)

print(type(a))
print(type(b))

b[3].append(4)
print(b)

a_1 = [4, 5, 6]
a_2 = [4, 5, 6]
b_1 = (4, 5, 6)
b_2 = (4, 5, 6)

print(id(a_1))
print(id(a_2))
print(id(b_1))
print(id(b_2))

for item in b:
    print(item)

e_1 = [10]
e_2 = [10,]

print(e_1)
print(e_2)

e_3 = (10)
e_4 = (10,)

print(e_3)
print(e_4)

my_tuple = tuple((int(x * 2) for x in a if isinstance(x, (int, float))))
print(my_tuple)
