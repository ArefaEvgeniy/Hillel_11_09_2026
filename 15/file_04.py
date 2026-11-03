import json
import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


if __name__ == "__main__":
    person_1 = Person("Alice", 30)
    person_2 = Person("Bob", 25)
    person_3 = Person("Charlie", 35)
    person_4 = Person("Diana", 28)

    bd = [person_1, person_2, person_3, person_4]

    for person in bd:
        print(person)

    with open("persons.txt", "w") as file:
        for person in bd:
            file.write(f"{person.name},{person.age}\n")

    print(bd[-1].greet())

    print([person.__dict__ for person in bd])

    with open("persons.json", "w") as file:
        json.dump([person.__dict__ for person in bd], file)

    with open("persons.pkl", "wb") as file:
        pickle.dump(bd, file)
