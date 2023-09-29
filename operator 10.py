import math

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

D = b**2 - 4*a*c

if D < 0:
    print("Уравнение не имеет корней.")
elif D == 0:
    x = -b / (2*a)
    print("Уравнение имеет 1 корень: ", x)
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Два корня: ", x1, "и", x2)
