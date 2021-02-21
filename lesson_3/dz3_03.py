"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif b < a < c:
        return a + c
    else:
        return b + c


unsorted_list = [float(input("Первый позиционный аргумент: ")), float(input("Второй позиционный аргумент: ")),
                 float(input("Третий позиционный аргумент: "))]
print(my_func(*unsorted_list))
