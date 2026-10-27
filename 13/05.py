class Animal:
    tail = True
    legs = 4

    def go(self):
        print('Object is going...')

    def jump(self):
        print('Object is jumping...')


class Dog(Animal):

    def say(self):
        print('Woof!')

    def bark(self):
        print('Bark!')


class Dolphin(Animal):

    def say(self):
        print('Click!')

    def go(self):
        print('Dolphin is swimming...')

    def click(self):
        print('Click! Click! Click!')


class Monster(Dog, Dolphin):
    pass


obj_1 = Monster()
obj_1.go()
obj_1.click()
obj_1.bark()
obj_1.say()
obj_1.jump()
