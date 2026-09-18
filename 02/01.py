
d = 1001
print(id(d))
d = d + 10
print(id(d))
print("d:", d)
b = 34.24
c = "Hello World"
a = 256
e = d
print("d:", d)
print("e:", e)
d = "Bob"
print("d:", d)
print("e:", e)
e = d
print("d:", d)
print("e:", e)
# print(a)
print(id(a))
print(id(b))
print(id(c))
print(id(d))

d_1 = 1011
d_2 = 1011
d_3 = 1011
d_4 = 1011
print(id(d_1))
print(id(d_2))
print(id(d_3))
print(id(d_4))

# PEP-8: Style Guide for Python Code

sale = 23
s = 23
