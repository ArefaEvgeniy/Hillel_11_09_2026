# class Dog:
class Dog(object):
    tail = True
    legs = 4

    def say(self):
        print('Woof!')

    def go(self):
        print('Dog is going...')


obj_1 = Dog()
obj_2 = Dog()

obj_1.say()
print(obj_1.legs)
obj_2.say()
obj_2.name = 'Bobby'
obj_2.legs = 3

Dog.legs = 5
obj_3 = Dog()
print(obj_1.legs)
print(obj_2.legs)
print(obj_3.legs)
print(obj_2.name)

print(obj_1.__dict__)
print(obj_2.__dict__)
print(obj_3.__dict__)
