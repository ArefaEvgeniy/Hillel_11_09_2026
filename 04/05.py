import copy

a = [2, 4, [55, 56, 89], 4]

b = copy.deepcopy(a)
c = copy.deepcopy(a)
d = copy.deepcopy(a)

print(id(a))
print(id(b))
print(id(c))
print(id(d))

b[2].pop(0)
d[2].reverse()
c[2].append(100)
print(a)
print(b)
print(c)
print(d)
