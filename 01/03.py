from langdetect import detect, detect_langs


print(detect("War doesn't show who's right, just who's left."))
print(detect("La guerra no muestra quién tiene razón, solo quién queda."))
print(detect("Цей текст надруковано написаний українською мовою."))
print(detect_langs("Otec matka syn."))
