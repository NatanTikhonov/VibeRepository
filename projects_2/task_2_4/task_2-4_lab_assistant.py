volume = float(input("Нужный объем раствора (мл): "))

salt_mass = volume * 0.009   # 0.9% NaCl
water_volume = volume        # объемом соли пренебрегаем

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли:  {salt_mass:.2f} г\n")
    file.write(f"Объем воды:  {water_volume} мл\n")

print("Рецепт записан в recipe.txt")
