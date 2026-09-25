a = [34, -56.563, "Hello", True, None, [1, ["a", "b"], 3], 99, 100]
b = []

print(a[0])
print(a[2])
print(a[-1])
print(len(a))
print(a[len(a)-1])
print(a[-3][1][-1])
# print(a[10])
# print(b[-1])

if len(a) > 5:
    print(a[5])

if len(b) > 5:
    print(b[5])
