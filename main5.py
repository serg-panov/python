# Sergey Panov
# Fifth exercise

"""
Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
"""


is_stop = False
total_sum = 0
while not is_stop:
    my_list = input("Please enter some digits or - (dash) symbol to stop:").split()
    for item in my_list:
        if item == '-':
            is_stop = True
            break
        try:
            total_sum = total_sum + float(item)
        except ValueError:
            print(f"ERROR: {item} is not valid number, skip it")
            continue
    print(f"Intermediate sum: {total_sum}")

print(f"Total sum: {total_sum}")
