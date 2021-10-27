# Sergey Panov
# Seventh exercise

"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
"""


class MyComplexMath:
    def __init__(self, cd):
        if not isinstance(cd, complex):
            raise ValueError("Argument must has complex type")
        self.__cd = cd

    def __add__(self, other):
        return MyComplexMath(self.__cd + other.__cd)

    def __radd__(self, other):
        # to work properly with sum function
        if not isinstance(other, self.__class__):
            return self
        return self.__add__(other)

    def __mul__(self, other):
        return MyComplexMath(self.__cd * other.__cd)

    def __str__(self):
        return str(self.__cd)


cd1 = MyComplexMath(1 + 1j)
cd2 = MyComplexMath(5 + 4j)
cd3 = MyComplexMath(2 + 7j)
print(cd1, "+", cd2, "=", cd1 + cd2)
my_list = [cd1, cd2, cd3]
print("sum of ", list(map(str, my_list)), "=", sum(my_list))
print(cd2, "*", cd3, "=", cd2 * cd3)
