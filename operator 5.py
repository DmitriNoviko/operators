a = float(input("Введите длину 1 стороны: "))
b = float(input("Введите длину 2 стороны: "))
c = float(input("Введите длину 3 стороны: "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")
