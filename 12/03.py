with open("test_file.txt", "rb") as vlad:
    new_text = vlad.read()

print(new_text)
print(new_text.decode("windows-1251"))
