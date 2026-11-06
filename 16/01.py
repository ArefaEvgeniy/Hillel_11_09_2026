class Person:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.__age = age

    def __getattribute__(self, item):
        print(f"Accessing attribute: {item}")
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            return None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be an integer")
        self.__age = value

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

# person_1.age = "Hello"
print(person_1.__dict__)
print(person_1.phone_number)
