bigger = int(input("Введите max число: "))
smaller = int(input("Введите min число: "))

if bigger % smaller == 0:
    print(bigger, "кратно", smaller)
else:
    print(bigger, "не кратно", smaller)
    remainder = bigger % smaller
    print("Остаток от деления:", remainder)
