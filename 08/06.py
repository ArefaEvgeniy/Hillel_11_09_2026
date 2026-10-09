def func(b, a, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("--------")


a = 34
b = 56
d = 1
func(a=d, b=100, c=a)
func(100, c=a, a=d)
