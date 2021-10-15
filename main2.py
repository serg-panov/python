# Sergey Panov
# Second exercise

"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
"""

res = []
with open("e2.txt", "r", encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        res.append(len(line.split()))

for n, l in enumerate(res):
    print("Line", n + 1, "has", l, "word(s)")
