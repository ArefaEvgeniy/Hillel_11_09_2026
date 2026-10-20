try:
    file = open("test_file.txt", "r", encoding="windows-1251")
    new_text = file.read()
finally:
    file.close()

print(new_text)
