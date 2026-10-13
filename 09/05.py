def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(955))

n = 1555
result = 1
while n > 1:
    result *= n
    n -= 1

print(result)
