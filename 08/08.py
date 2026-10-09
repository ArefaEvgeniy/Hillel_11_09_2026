def func(*args):
    sum = 0
    print("args:", args)
    for item in args:
        sum += item
    print("sum:", sum)
    print("--------")


a = 34
b = 56
d = 1
func(12, 33)
func(a, d, b, 44, 66, 77)
func(1, 2, 3)
func(3)
func(0)
