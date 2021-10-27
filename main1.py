# Sergey Panov
# First exercise

"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""


class Date:
    str_date = ''

    def __init__(self, st):
        Date.str_date = st

    @classmethod
    def parse(cls):
        return list(map(int, cls.str_date.split('-')))

    @staticmethod
    def validate(st):
        validators = [lambda x: True if 1 <= x <= 31 else False, lambda x: True if 1 <= x <= 12 else False,
                      lambda x: True if x >= 1900 else False]
        for pos, el in enumerate(Date.parse()):
            if not validators[pos](el):
                raise ValueError(f"Invalid number in position {pos + 1}")
        return True


dt = Date('01-01-2021')
Date.validate(Date.str_date)
#dt = Date('32-01-2021')
#Date.validate(Date.str_date)
#dt = Date('01-13-2021')
#Date.validate(Date.str_date)
#dt = Date('01-01-11')
#Date.validate(Date.str_date)
