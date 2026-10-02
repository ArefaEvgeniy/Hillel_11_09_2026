template = "My name is %s and I am %s years old. %s is a good person."

name = "John"
age = 30

print(template)

new_str = template % (name, age, name)
print(new_str)
print(template % ("Alice", 25, "Alice"))
