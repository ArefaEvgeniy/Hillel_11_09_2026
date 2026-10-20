with open("test_file.txt") as file:
    print(file.read(10))
    print(file.read(15))
    print(file.read(14))
    file.seek(0)
    print(file.read(5))

print("--------------------")
with open("test_file.txt") as file:
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.readline().strip())

print("--------------------")
with open("test_file.txt") as file:
    print(file.readlines())
