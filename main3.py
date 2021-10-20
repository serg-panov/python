# Sergey Panov
# Third exercise

"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""

from itertools import cycle


class Box:
    def __init__(self, cells):
        self.__cells = int(cells)

    def __add__(self, other):
        return Box(self.__cells + other.__cells)

    def __radd__(self, other):
        # to work properly with sum function
        if not isinstance(other, Box):
            return self
        return self.__add__(other)

    def __sub__(self, other):
        if self.__cells <= other.__cells:
            print("Invalid result")
            return self
        return Box(self.__cells - other.__cells)

    def __mul__(self, other):
        return Box(self.__cells * other.__cells)

    def __truediv__(self, other):
        return Box(self.__cells // other.__cells)

    def make_order(self, i):
        return ('*' * int(i) + "\n") * (self.__cells // int(i)) + '*' * (self.__cells % int(i))


box1 = Box(12)
print(box1.make_order(5))
box2 = Box(15)
print(box2.make_order(5))
box3 = box1 + box2
print(box3.make_order(5))
box3 = box1 - box2
print(box3.make_order(5))
box3 = box2 - box1
print(box3.make_order(5))
box3 = box2 * box1
print(box3.make_order(179))
box3 = box2 / box1
print(box3.make_order(5))
