# Пишем информацию о себе в файл output.txt (он появится рядом со скриптом)
f = open("output.txt", "w", encoding="utf-8")
print("Фамилия: Тихонов", file=f)
print("Имя: Натан", file=f)
print("Группа: 202.1", file=f)
print("Год поступления: 2026", file=f)
f.close()

print("Готово, смотри файл output.txt")
