# Sergey Panov
# Second exercise

"""
Реализовать класс Road (дорога).
- определить атрибуты: length (длина), width (ширина);
- значения атрибутов должны передаваться при создании экземпляра класса;
- атрибуты сделать защищёнными;
- определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
- использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
- проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__weight = 25  # 25 kg for 1 cm

    def calc(self, depth):
        return self._length * self._width * self.__weight * depth


road1 = Road(20, 5000)
print(road1.calc(5) / 1000, 'tons')
print(road1.calc(50) / 1000, 'tons')
road2 = Road(50, 5000)
print(road2.calc(5) / 1000, 'tons')
print(road2.calc(50) / 1000, 'tons')
