donor = input("Группа крови донора (I, II, III, IV): ").strip().upper()
patient = input("Группа крови пациента (I, II, III, IV): ").strip().upper()

groups = ["I", "II", "III", "IV"]

if donor not in groups or patient not in groups:
    print("Такой группы крови не существует")
elif donor == patient or donor == "I":
    print("Переливание возможно")
else:
    print("Переливание невозможно")
