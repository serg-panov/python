# Sergey Panov
# Sixth exercise

"""
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
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


print(int_func('text'))
print(int_func('tExt'))
print(int_func('text123'))
print(int_func(''))
