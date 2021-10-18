# Sergey Panov
# Fifth exercise

"""
Реализовать класс Stationery (канцелярская принадлежность).
- определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
- создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
- в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
- создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        super().__init__("ручка")

    def draw(self):
        print(f"Отрисовка {self.title}")


class Pencil(Stationery):
    def __init__(self):
        super().__init__("карандаш")

    def draw(self):
        print(f"Отрисовка {self.title}")


class Handle(Stationery):
    def __init__(self):
        super().__init__("маркер")

    def draw(self):
        print(f"Отрисовка {self.title}")


for i in [Stationery('принадлежность'), Pen(), Pencil(), Handle()]:
    i.draw()
