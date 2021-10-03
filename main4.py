# Sergey Panov
# Fourth exercise

"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

my_str = input("Please enter sentence: ")
my_list = my_str.split()

for i in range(len(my_list)):
    print(i + 1, my_list[i][0:10])
