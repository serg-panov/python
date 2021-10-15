# Sergey Panov
# Third exercise

"""
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

total = 0
cnt = 0
with open("e3.txt", "r", encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        cnt = cnt + 1
        n, s = line.split()
        if float(s) < 20000:
            print(n, "has salary less than 20000")
        total = total + float(s)

if cnt > 0:
    print(f"Avg salary: {total / cnt}")
