a = 100

if a > 0:
    result = a / 2
else:
    result = abs(a)
print(result)

print("--------------")

result_2 = a / 2 if a > 0 else abs(a)
print(result_2)
