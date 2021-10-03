# Sergey Panov
# Second exercise

"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = []
while True:
    el = input("Please enter new element of list, enter empty string to stop: ")
    if len(el) != 0:
        my_list.append(el)
    else:
        break

for i in range(len(my_list) // 2):
    my_list[2 * i], my_list[2 * i + 1] = my_list[2 * i + 1], my_list[2 * i]

print(my_list)
