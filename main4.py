# Sergey Panov
# Fourth exercise

"""
Программа принимает действительное положительное число x и целое отрицательное число
y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
"""


def my_func(x, y):
    return x ** y;


def my_func2(x, y):
    x = (x, 1 / x)[y < 0]
    res = 1
    while abs(y) > 0:
        res = res * x
        y = abs(y) - 1
    return res


x, y = None, None
while True:
    if x is None:
        try:
            x = float(input("Please enter positive number X: "))
            if x < 0:
                print("X must be any positive number")
                x = None
                continue
        except ValueError:
            print("X must be any positive number")
            continue
    if y is None:
        try:
            y = int(input("Please enter negative integer Y: "))
            if y >= 0:
                print("Y must be negative integer")
                y = None
                continue
        except ValueError:
            print("Y must be negative integer")
            continue
    break


print(my_func(x, y))
print(my_func2(x, y))
