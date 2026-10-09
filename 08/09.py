def func(**kwargs):
    print("kwargs:", kwargs)
    print("--------")


a = 34
b = 56
d = 1
func(a=12, b=33)
func(a=a, b=d, c=b, d=44, e=66, f=77)
func(a=3)
func()
