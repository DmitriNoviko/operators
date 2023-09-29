a = int(input("Введите a число: "))
b = int(input("Введите b число: "))
c = int(input("Введите c число: "))

if a == b or b == c or a == c:
    print("Ошибка: есть = числа")
else:
    if (a > b and a < c) or (a > c and a < b):
        print("middle число:", a)
    elif (b > a and b < c) or (b > c and b < a):
        print("middle число:", b)
    else:
        print("middle число:", c)
