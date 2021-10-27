# Sergey Panov
# Second exercise

"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivision(Exception):
    pass


try:
    a, b = list(map(float, input("Please enter two numbers: ").split()[0:2]))
    if b == 0:
        raise MyZeroDivision
    print(f"Division result {a / b}")
except ValueError as err:
    print(err)
except MyZeroDivision:
    print("Second number must no be 0")
else:
    print("Done")
