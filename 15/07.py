import pickle

from file_04 import Person


with open("persons.pkl", "rb") as file:
    bd = pickle.load(file)


print(bd[-1].greet())
