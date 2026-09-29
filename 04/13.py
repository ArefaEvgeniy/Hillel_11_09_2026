import random

print(random.random())
print(random.randint(1, 6))

seq = ["apple", "banana", "cherry", "date"]
print(random.choice(seq))

random.shuffle(seq)
print(seq)
