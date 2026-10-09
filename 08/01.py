def func(a, b):
    def inner_func(x, y):
        return (x + y) * 2

    result = inner_func(a, b)
    if result < 0:
        return abs(result) * 2
    else:
        return result


print(func)
func(12, 45)
