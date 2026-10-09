def func(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("--------")


d = (5, 66, 3)

func(d[0], d[1], d[2])
func(*d)
