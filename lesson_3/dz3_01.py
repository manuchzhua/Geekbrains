"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(dividend, divider):
    try:
        quotient = dividend / divider
        return round(quotient, 3)
    except ZeroDivisionError:
        return "Деление на ноль невозможно"


print(division(float(input("Введите делимое: ")), float(input("Введите делитель: "))))
