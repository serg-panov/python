# Sergey Panov
# Second exercise
"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

in_seconds_var = int(input("Please enter seconds: "))
hours = in_seconds_var // 3600
minutes = (in_seconds_var - hours * 3600) // 60
seconds = in_seconds_var - hours * 3600 - minutes * 60

print(f"Time is {hours:02}:{minutes:02}:{seconds:02}")