"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def data_user(name, last_name, year_of_birth, city, email, tel):
    print(
        f"Имя:{name} Фамилия:{last_name} Год рождения:{year_of_birth} Год рождения:{city} Email:{email} Телефон:{tel}"
    )


m = [
    input("Имя: "), input("Фамилия: "), input("Год рождения: "), input("Город проживания: "), input("Email: "),
    input("Телефон: ")
]
data_user(name=m[0], last_name=m[1], year_of_birth=m[2], city=m[3], email=m[4], tel=m[5])
