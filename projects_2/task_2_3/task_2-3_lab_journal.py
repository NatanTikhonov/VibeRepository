researcher = input("ФИО исследователя: ")
date = input("Дата: ")
experiment = input("Название эксперимента: ")
conclusion = input("Вывод: ")

line = "+" + "-" * 50 + "+"

with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(line + "\n")
    file.write(f"| {'Электронный лабораторный журнал':<48} |\n")
    file.write(line + "\n")
    file.write(f"| {'ФИО исследователя : ' + researcher:<48} |\n")
    file.write(f"| {'Дата              : ' + date:<48} |\n")
    file.write(f"| {'Эксперимент       : ' + experiment:<48} |\n")
    file.write(line + "\n")
    file.write(f"| {'Вывод:':<48} |\n")
    file.write(f"| {conclusion:<48} |\n")
    file.write(line + "\n")

print("Журнал сохранен в journal.txt")
