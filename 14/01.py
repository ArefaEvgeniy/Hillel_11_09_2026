print("Hello World")
a = [100, 10, -100]
b = "34"

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
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    c = 0
else:
    print("no error")
finally:
    print("finally")


print(f"c: {c}")
print("end")
