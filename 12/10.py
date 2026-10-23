def swim(self):
    print('Swimming...')


class Animal:
    tail = True
    legs = 4

    def go(self):
        print('Object is going...')


class Dog(Animal):

    def say(self):
        print('Woof!')

    def bark(self):
        print('Bark!')


class Cat(Animal):

    def say(self):
        print('Meow!')

    def climb(self):
        print('Climbing...')


obj_1 = Cat()
obj_1.go()
print(obj_1.legs)
Dog.legs = 5
print(obj_1.legs)
obj_1.say()
obj_2 = Cat()
obj_2.swim = swim.__get__(obj_2, Cat)
obj_2.swim()
