# Sergey Panov
# Fourth exercise

"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

eng2rus_translate = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                     'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
with open("e4.txt", 'r', encoding='utf-8') as f, open("e4-rus.txt", 'w') as fw:
    while True:
        line = f.readline();
        if not line:
            break
        words = line.split()
        print(eng2rus_translate.get(words[0].lower()).capitalize(), " ".join(words[1:]), file=fw)
