my_dict = {"name": "Alice", "age": 30, "city": "New York"}

print(len(my_dict))  # Output: 3
print(my_dict["name"])  # Output: Alice

if "city" in my_dict:
    print(my_dict["city"])

if "phone" in my_dict:
    print(my_dict["phone"])

print(my_dict.get("phone", "Not Found"))
print(my_dict.get("city", "Not Found"))

my_dict.update({"age": 31, "phone": "123-456-7890"})
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

print("---------")
for item in my_dict:
    print(item)
print("---------")
for item in my_dict.values():
    print(item)
print("---------")
for key, value in my_dict.items():
    print(f"{key} -> {value}")
