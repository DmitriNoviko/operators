import math

x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
r = float(input("Введите r круга: "))

d = math.sqrt(x ** 2 + y ** 2)

if d <= r:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")
