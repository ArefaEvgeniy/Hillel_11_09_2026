name = "Bob"


def func_1():
    def func_3():
        name = "Charlie"
        print("go,  " + name)
        return name

    name = "Alice"
    new_name = func_3()
    print("Hello, " + name + "!")
    return new_name


def func_2():
    print("hi, " + name)


print(name + "!")
name = func_1()
func_2()
print("Bye, " + name)
