# Sergey Panov
# First exercise

"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.
"""


def my_div(arg1, arg2):
    if arg2 == 0:
        print("ERROR: arg2 must not be 0.")
        return
    return arg1/arg2


def my_div2(arg1, arg2):
    try:
        return arg1/arg2
    except ZeroDivisionError:
        print("ERROR: arg2 must not be 0.")
    return


print(my_div(4, 2))
print(my_div(4, 0))
print(my_div(3, 2))
print(my_div(3, 0))
