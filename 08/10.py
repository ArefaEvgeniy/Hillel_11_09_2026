def func(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
    print("--------")


a = 34
b = 56
d = 1
func(12, b=33)
func(12, 23, 666, 77)
func(a, d, b, d=44, e=66, f=77)
func(a=3, e=66)
func()
