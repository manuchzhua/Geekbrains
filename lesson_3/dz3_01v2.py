def div(x, y):
    try:
        return round(x / y, 3)
    except ZeroDivisionError:
        return "Деление на ноль невозможно"


while True:
    x = input('Введите делимое или нажмите q для выхода\n')
    try:
        x = float(x)
    except ValueError:
        if x.lower() == 'q':
            print('До свидания')
            break
        print('Ошибка ввода команды')
        continue

    y = input('Введите делитель или нажмите q для выхода\n')
    try:
        y = float(y)
    except ValueError:
        if y.lower() == 'q':
            print('До свидания')
            break
        print('Ошибка ввода команды')
        continue

    print(div(x, y))
