total_capsules = int(input("Введите общее количество произведенных капсул: "))
pack_size = int(input("Введите количество капсул в одной упаковке: "))

full_packs = total_capsules // pack_size
left_capsules = total_capsules % pack_size

print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packs}")
print(f"Остаток капсул:\t\t{left_capsules}")
