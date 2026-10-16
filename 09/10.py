def func(a, b):
    res = (a + b)**2
    yield res
    res += 45
    yield res
    res += 100
    yield res


my_gen = func(10, 20)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
