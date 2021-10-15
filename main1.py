# Sergey Panov
# First exercise

"""
Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.
"""

with open("e1.txt", "w") as f:
    while True:
        s = input("Please enter string to save to file: ")
        if len(s) == 0:
            break
        print(s, file=f)
