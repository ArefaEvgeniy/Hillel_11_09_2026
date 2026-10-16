def decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")

    return wrapper


@decorator  # along_func = decorator(along_func)
def along_func():
    print("I'm along_func")


along_func()
