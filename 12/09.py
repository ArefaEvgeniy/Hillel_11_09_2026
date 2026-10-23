class Dog:
    tail = True
    legs = 4

    def say(self):
        print('Woof!')

    def go(self):
        print('Object is going...')

    def bark(self):
        print('Bark!')


class Cat(Dog):

    def say(self):
        print('Meow!')

    def climb(self):
        print('Climbing...')

    def bark(self):
        pass


obj_1 = Cat()
obj_1.go()
print(obj_1.legs)
Dog.legs = 5
print(obj_1.legs)
obj_1.bark()
obj_1.say()
