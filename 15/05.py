from file_04 import Person

with open("persons.txt", "r") as file:
    data = file.readlines()

print(data)

bd = []
for person in data:
    name, age = person.strip().split(",")
    bd.append(Person(name, int(age)))

print(bd[-1].greet())
