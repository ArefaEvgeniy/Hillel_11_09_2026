def func(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("--------")


d = {"b": 1, "a": 2, "c": 3}

func(**d)  # b=1, a=2, c=3
