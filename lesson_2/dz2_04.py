# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.


my_list = []
num = 1
new_my_str = input("Введите строку из нескольких слов, разделённых пробелами: ")

# удаление лишних пробелов
new_my_str.split()
my_str = ' '.join(new_my_str.split())

for el in range(my_str.count(' ') + 1):
    my_list = my_str.split()
    if len(str(my_list)) <= 10:
        print(f" {num} {my_list[el]}")
        num += 1
    else:
        print(f" {num} {my_list[el][0:10]}")
        num += 1
