data = [34, 0, -34, "rrr", "EWRTTGTFG", 100]


def func(a):
    if isinstance(a, int):
        return a * 2
    else:
        return len(a)


print(list(map(func, data)))
print(list(map(lambda a: a * 2 if isinstance(a, int) else len(a), data)))
