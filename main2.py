# Sergey Panov
# Second exercise

"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class ClothesInterface:
    @abstractmethod
    def info(self):
        pass


class Clothes(ClothesInterface):
    def __init__(self):
        self.__name = "заготовка"
        self.__consumes = 0

    def info(self):
        return f"{self.__name} consume {self.__consumes} materials"

    def __setattr__(self, key, value):
        if key == 'v':
            self.__name = "пальто"
            self.__consumes = int(value) / 6.5 + 0.5
        elif key == 'h':
            self.__name = "костюм"
            self.__consumes = 2 * int(value) + 0.3
        else:
            self.__dict__[key] = value

    @property
    def consumes(self):
        return self.__consumes


c1 = Clothes()
c1.v = 13
print(f"{c1.info()}")
print(c1.consumes)

c2 = Clothes()
c2.h = 1
print(f"{c2.info()}")
print(c2.consumes)

c3 = Clothes()
c3.l = 1
print(f"{c3.info()}")
