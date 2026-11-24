proteins = float(input("Белки (г): "))
fats = float(input("Жиры (г): "))
carbs = float(input("Углеводы (г): "))

calories = proteins * 4 + fats * 9 + carbs * 4

print(f"Калорийность продукта: {calories:.1f} ккал")
