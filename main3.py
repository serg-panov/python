# Sergey Panov
# Third exercise

"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

my_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
my_dist = {'1': 'зима', '2': 'зима', '3': 'весна', '4': 'весна', '5': 'весна', '6': 'лето', '7': 'лето', '8': 'лето',
           '9': 'осень', '10': 'осень', '11': 'осень', '12': 'зима'}
while True:
    month = input("Please enter month number from 1 till 12: ")
    if month.isdigit() and 0 < int(month) <= 12:
        break
    else:
        print("Invalid input. Try again.")

print(my_list[int(month) - 1])
print(my_dist[month])
