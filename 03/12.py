a = 0

if a > 0:
    print("a is positive")
elif a == 0:
    print("a is zero")
else:
    print("a is not positive")

print("--------------")

print("a is positive") if a > 0 else (print("a is zero") if a == 0 else print("a is not positive"))
