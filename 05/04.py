my_str = "This    is a  long string          that is    split.\nThis  is a new     line."
print(my_str)
my_str = my_str.replace("\n", "\\n")
new_list = my_str.split()
print(new_list)
new_str = " ".join(new_list)
new_str = new_str.replace("\\n", "\n")
print(new_str)
