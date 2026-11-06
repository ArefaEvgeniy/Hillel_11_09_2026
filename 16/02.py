class Person:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def __setattr__(self, attr_name, attr_value):
        if attr_name == "age":
            if not isinstance(attr_value, int) or attr_value <= 0:
                print("Age must be a positive integer")
                self.__dict__[attr_name] = None
                return None
        self.__dict__[attr_name] = attr_value

    @property
    def full_name(self):
        return f"{self.first_name} {self.second_name}"

    @full_name.setter
    def full_name(self, name):
        if len(name.split()) != 2:
            raise ValueError("Full name must contain first and second name")
        self.first_name, self.second_name = name.split()

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.second_name = None


person_1 = Person("John", "Doe", -4565)
print(person_1.first_name)
print(person_1.second_name)
print(person_1.full_name)
print("--------------")

person_1.second_name = "Smith"
print(person_1.first_name)
print(person_1.second_name)
print(person_1.full_name)
print(person_1.__dict__)
print("--------------")

person_1.full_name = "Robert Brown"
print(person_1.first_name)
print(person_1.second_name)
print(person_1.full_name)
print(person_1.__dict__)

del person_1.full_name
print(person_1.__dict__)
print("--------------")

person_1.age = "Hello"
print(person_1.__dict__)
print("--------------")

person_1.age = 45
print(person_1.age)
print(person_1.__dict__)
