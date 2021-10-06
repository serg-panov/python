# Sergey Panov
# Second exercise

"""
Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой.
"""


def show_user_info(**kwargs):
        print(f"Fist name: {kwargs.get('fname')}, Last name: {kwargs.get('lname')}, "
              f"Year of birth: {kwargs.get('year_of_birth')}, City: {kwargs.get('city')}, "
              f"Email: {kwargs.get('fname')}, Phone: {kwargs.get('phone')}")


show_user_info(fname="Ivan", lname="Ivanov", year_of_birth="1990", city="Moscow",
               email="ivan@ivanov.org", phone="79991234567")
show_user_info(fname="Ivan", lname="Ivanov")
