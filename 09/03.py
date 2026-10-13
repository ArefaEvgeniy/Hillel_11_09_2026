def func(string):
    """
    This is a closure function that takes a string as an argument
    and returns an inner function that prints "Hello, World!" when called.
    :param string: this a text
    :return: adress of the inner function
    """
    def inner_func():
        print("Hello, World!")

    print(string)

    return inner_func


my_func = func("This is a closure example.")
print(my_func)
my_func()

print(func.__doc__)
