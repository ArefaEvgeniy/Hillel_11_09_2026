age = 89
print("answer:", age)
print(age)
print()
print(999)
print("answer:", age, 678, "hello", sep="!!!", end=" ")
print("answer:", age, end=" ")
print(999)
print("Hello")

f = open("test.txt", "w")
print("answer:", age, 678, "hello", sep="!!!", file=f)
f.close()
