# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Вариант 1
seasons_list = ('Зима', 'Весна', 'Лето', 'Осень')
seasons_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень'}
while True:
    month = (input("Введите номер месяца: "))
    if month.isdigit():
        month = int(month)
        break
    print('Ошибка ввода, Вы ввели не число')

if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(0))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(1))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(2))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(3))
    print(seasons_list[3])
else:
    print("Такого месяца не существует")
