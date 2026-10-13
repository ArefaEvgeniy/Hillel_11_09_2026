data = [34, 0, -34, "rrr", "EWRTTGTFG", 100]


def func(a):
    return isinstance(a, int)


print(list(filter(func, data)))
print(list(filter(lambda a: isinstance(a, int), data)))
