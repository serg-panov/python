# Sergey Panov
# First exercise

"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта
для конкретных значений необходимо запускать скрипт с параметрами.
"""


from sys import argv, exit

if len(argv) < 4:
    print("Not enough arguments, script expect 3 mandatory integer arguments.")
    exit(1)

print(f"Salary: {int(argv[1])*int(argv[2])+int(argv[3])}")
