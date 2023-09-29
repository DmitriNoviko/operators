a = int(input("Введите a число: "))
b = int(input("Введите b число: "))
c = int(input("Введите c число: "))

if a > b and a > c:
    print("max число:", a)
elif b > a and b > c:
    print("max число:", b)
else:
    print("max число:", c)
