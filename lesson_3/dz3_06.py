"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


# Решение первой части применимо и ко второй. Задание не понял.
# По заданию не понятно как можно использовать написанную ранее функцию если там предполагалось вводить одно слово.

# Часть первая
def func(a):
    return a.title()


print(func(input("Введите слово из маленьких латинских букв: ")))


# Часть вторая
# Может по заданию подразумевали разложение на список и сбор в строку?
def my_func(b):
    separate_word = b.split(' ')
    total = []
    for i in separate_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    print(' '.join(total))


(my_func(input("Введите слова из маленьких латинских букв: ")))