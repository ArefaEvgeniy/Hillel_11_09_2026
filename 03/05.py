a = 1500

if a > 1000:
    print("a is greater than 1000")
    a = a ** 0.5
elif a > 100:
    print("a is greater than 100")
    a = a ** 0.5
elif a > 0:
    print("a is positive")
    a = a / 2
elif a == 0:
    print("a is zero")
elif a < -10:
    print("a is negative")
    a = a * 2
else:
    print("a is something else")

print("a is now:", a)
print("END")
