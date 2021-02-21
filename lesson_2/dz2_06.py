# *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
#
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

product = int(input("Введите количество разновидностей товаров: "))
n = 1
dict_dz = []
list_dz = []
# analysis_dz = {}
while n <= product:
    dict_dz = dict(
        {'Название': input(f"Введите название '{n}' товара: "), 'Цена': input(f"Введите цену '{n}' товара: "),
         'Количество': input(f"Введите количество '{n}' товара: "),
         'Ед': input(f"Введите единицу измерения '{n}' товара: ")})
    list_dz.append((n, dict_dz))
    n += 1
for n in list_dz:
    print(n)

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {“название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]}

product = []
product_detail = {"Название": '', "Цена": '', "Количество": '', "Ед": ''}
analytics = {"Название": [], "Цена": [], "Количество": [], "Ед": []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для продолжения нажмите 'Enter', для анализа введите 'A', Для выхода введите 'Q': ").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        for key, value in analytics.items():
            print(f'{key[:25]}: {value}')
    for f in product_detail.keys():
        feature_ = input(f'Введите "{f}" товара: ')
        product_detail[f] = int(feature_) \
            if (f == "Цена" or f == "Количество") \
            else feature_
        analytics[f].append(product_detail[f])
    product.append((num, product_detail))