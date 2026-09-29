a = 10

result = []
for item in range(3, a+1, 3):
    result.append(item)

print("Result:", result)


result = []
for _ in range(a):
    result.append("*")

print("Result:", result)
