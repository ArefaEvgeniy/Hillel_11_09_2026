def func(a, b):
    try:
        print("start")
        c = a[2] / b
        print("continue")
    except (ValueError, ZeroDivisionError):
        c = 0
    except IndexError:
        c = None
    except LookupError:
        c = -1

    print("function continue")
    return c


print("Hello World")
a = [100, 10, -100]
b = "0"

try:
    res = func(a, b)
except TypeError:
    res = None

print(f"res: {res}")
print("end")
