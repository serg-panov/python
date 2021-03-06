# Sergey Panov
# Fifth exercise
"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

income = int(input("Введите размер выручки (целое положительное число): "))
expence = int(input("Введите размер издержек (целое положительное число): "))
if income > expence:
    print(f"Вы работаете с прибылью! Рентабельность {(1-expence/income)*100:.2f}%")
    employes = int(input("Введите кол-во сотрудникоа (целое положительное число): "))
    print(f"Прибыль в расчете на одного сотрудника {(income - expence) / employes}")
elif income == expence:
    print("Вы работаете с 0-й прибылью!")
else:
    print("Вы работаете в убыток!")
