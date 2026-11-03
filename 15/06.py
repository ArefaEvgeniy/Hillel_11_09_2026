import json

from file_04 import Person

with open("persons.json", "r") as file:
    data = json.load(file)

bd = []
for person in data:
    bd.append(Person(person["name"], person["age"]))

print(bd[-1].greet())
