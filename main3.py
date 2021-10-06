# Sergey Panov
# Third exercise

"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    try:
        return sum(sorted([arg1, arg2, arg3], reverse=True)[:2])
    except TypeError as err1:
        print(f"ERROR: {err1}")


print(my_func(1, 2, 3))
print(my_func(3, 2, 3))
print(my_func(3, 2, 'qweqw'))
print(my_func('1', '23', '456'))
