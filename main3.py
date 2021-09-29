# Sergey Panov
# Third exercise
"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

in_var = int(input("Please enter int value: "))
double = int(str(in_var) * 2)
triple = int(str(in_var) * 3)
print(f"{in_var} + {double} + {triple} = {in_var + double + triple}")
