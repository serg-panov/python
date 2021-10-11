# Sergey Panov
# Fifth exercise

from functools import reduce

"""
Реализовать формирование списка, используя функцию range() и возможности генератора. В
список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить
результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""


#def my_multiplication()

my_list = [el for el in range(100, 1001) if el%2 == 0]
print(reduce(lambda prev_el, el: prev_el * el, my_list))
