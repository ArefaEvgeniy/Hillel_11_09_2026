import copy

a = [2, 4, 67, 4]

b = a.copy()
c = a[:]
d = copy.copy(a)

print(id(a))
print(id(b))
print(id(c))
print(id(d))

b.pop(0)
d.reverse()
c.append(100)
print(a)
print(b)
print(c)
print(d)
