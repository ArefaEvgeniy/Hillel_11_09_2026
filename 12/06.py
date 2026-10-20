text = "Це тестовий, текст для перевірки коду."

with open("test_file_2.txt", "w", encoding="utf-8") as file:
    file.write(text)

with open("test_file_2.txt", "rb") as file:
    new_text = file.read(6)

print(new_text)
print(new_text.decode("utf-8"))

# with open("test_file_2.txt", "rb") as file:
#     new_text = file.read(7)
#
# print(new_text)
# print(new_text.decode("utf-8"))
