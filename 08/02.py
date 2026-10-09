name = "Bob"


def func_1():
    def func_3():
        global name
        name = "Charlie"
        print("go,  " + name)

    name = "Alice"
    func_3()
    print("Hello, " + name + "!")


def func_2():
    print("hi, " + name)


print(name + "!")
print(func_1())
func_2()
print("Bye, " + name)
