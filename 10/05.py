def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result

    return wrapper


@decorator
def along_func():
    print("I'm along_func")


@decorator
def sum(a, b):
    return a + b


along_func()
print("--------------------")
print(sum(10, 35))
