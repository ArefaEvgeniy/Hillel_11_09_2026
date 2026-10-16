def func(a):
    def inner(b):
        return a + b

    return inner


new_func = func(10)
print(new_func(5))
