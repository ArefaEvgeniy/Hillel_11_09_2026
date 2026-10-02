template = "My name is {} and I am {} years old. {} is a good person."
template_2 = "My name is {0} and I am {1} years old. {0} is a good person."
template_3 = "My name is {name} and I am {age} years old. {name} is a {rrr} person."

name = "John"
age = 30

print(template)

new_str = template.format(name, age, name, "TTT")
print(new_str)
print(template.format("Alice", 25, "Alice"))
print(template_2.format("Alice", 25))

print(template_3.format(name="Alice", age=age, rrr="good"))
