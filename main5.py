# Sergey Panov
# Fifth exercise

"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""

import random

# write file with random integers
with open("e5.txt", 'w') as f:
    print(" ".join([str(random.randint(0, 50)) for e in range(10)]), file=f)

# calc sum
with open("e5.txt", 'r', encoding='utf-8') as f:
    print(sum([int(e) for e in f.readline().split()]))
