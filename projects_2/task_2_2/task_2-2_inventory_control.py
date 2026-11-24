reagent_name = input("Название реактива: ")
reagent_count = int(input("Количество (шт): "))

report = (f"Реактив {reagent_name} поступил на склад "
          f"в количестве {reagent_count} шт.")
print(report)

# Дополнительно: сохраняем отчет в файл
with open("inventory.txt", "w", encoding="utf-8") as file:
    file.write(report + "\n")
