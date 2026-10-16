# Написать декоратор, который выдаст:
# </----------\>
# помидоры
# --ветчина--
# ~салат~
# <\______/>

def decorator(func):
    def wrapper():
        print("помидоры")
        func()
        print("~салат~")

    return wrapper


def decorator_2(func):
    def wrapper():
        print("</----------\\>")
        func()
        print("<\\______/>")

    return wrapper


@decorator_2
@decorator
def sandwich(food="--ветчина--"):
    print(food)


sandwich()
