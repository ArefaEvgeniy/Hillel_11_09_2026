def func(a: int, b: int | float, c: str, d: list) -> str:
    res = round(((a + b)**2) / a)
    result = str(res) + c
    print(result)
    return result in d


print(func(10.23, 34.5, " is the result", "200.0 is the result"))
print(func.__annotations__)
