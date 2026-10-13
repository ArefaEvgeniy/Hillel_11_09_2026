def func(a, b):
    if (a + b) > 100:
        return (a + b) / 2
    else:
        return (a + b) * 2


print(func(10, 20))
print((lambda x, y: (x + y) / 2 if (x + y) > 100 else (x + y) * 2)(10, 20))

func_2 = lambda x, y: (x + y) / 2
print(func_2(10, 20))
