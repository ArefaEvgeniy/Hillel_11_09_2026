class MyString(str):
    def __sub__(self, other):
        if isinstance(other, str):
            return self.replace(other, "", 1)
        return NotImplemented


a = MyString("Hello world!")
b = MyString("l")

print(a.upper())
print(a - b)
