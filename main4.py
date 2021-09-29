# Sergey Panov
# Fourth exercise
"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

in_var = int(input("Please positive int value: "))
new_var = in_var
max_val = 0
while new_var > 0:
    one_digit = new_var % 10
    if max_val < one_digit:
        max_val = one_digit
    new_var = new_var // 10
print(f"Max digit: {max_val}")
