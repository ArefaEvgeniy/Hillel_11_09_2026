text = "Новий тестовий текст для перевірки коду."

with open("test_file_3.txt", "wb") as file:
    file.write(text.encode("utf-8"))

with open("test_file_3.txt", "ab") as file:
    file.write(text.encode("utf-16"))

with open("test_file_3.txt", "ab") as file:
    file.write(text.encode("windows-1251"))

with open("test_file_3.txt", "rb") as file:
    new_text = file.read()

print(new_text.decode("utf-16", errors="ignore"))
