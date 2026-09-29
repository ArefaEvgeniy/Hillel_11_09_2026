my_string_1 = 'I like Python'
my_string_2 = "I like Python"
my_string_3 = "567"
my_string_4 = 'I like "Python"'
my_string_5 = "I like's Python"
my_string_6 = "I like's"
my_string_7 = ' "Python"'
my_string_8 = my_string_6 + my_string_7
my_string_9 = "I\tlike's\n \"Python\""
my_string_10 = r"\n - this is a new line; \t - this is a tab"
my_string_11 = r"I like's \"Python\" \n - this is a new line"
my_string_12 = "This is a long string that is split.\nAcross multiple lines for better readability.\nThis is a new line"
my_string_13 = """This is a long string that is split. 
Across multiple lines for better readability. 
        This is a new line"""

print(my_string_1)
print(my_string_2)
print(my_string_1 == my_string_2)
print(my_string_3)
print(type(my_string_1))
print(type(my_string_2))
print(type(my_string_3))
a = str(45 + 67)
print(a)
print(type(a))
print(my_string_4)
print(my_string_5)
print(my_string_1 + " " + my_string_3)
print(my_string_8)
print(my_string_9)
print(my_string_10)
print(my_string_11)
print(my_string_12)
print(my_string_13)

a = "Python"

print(a + a + a)
print(a * 3)
print(3 * a)

a = 10
b = "12"

print(a + int(b))
print(str(a) + b)
