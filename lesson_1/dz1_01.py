import math

name = (input("Введите Ваше имя: "))
print(f"{name}, введите стороны прямоугольного треугольника")
a = int(input("Высота = "))
b = int(input("Основание = "))
c = round(math.sqrt(a ** 2 + b ** 2), 2)
L = round(math.sqrt(2) * (a * b / (a + b)), 2)
print("{}, биссектриса прямоугольного треугольника = {}, а гипотенуза = {}.".format(name, L, c))
