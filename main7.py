# Sergey Panov
# Seventh exercise

"""
Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
написанную ранее функцию int_func().
"""


def int_func(txt):
    my_list = list(txt)
    for i in my_list:
        if i.isalnum() and i.isupper():
            print(f"word must contain only lower case")
            return

    if len(my_list) > 0:
        my_list[0] = my_list[0].upper()
    return ''.join(my_list)


my_str = input("Please enter words in lower case: ")
my_list = []
for i in my_str.split():
    my_list.append(int_func(i))
print(f"{' '.join(my_list)}")
