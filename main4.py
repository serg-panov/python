# Sergey Panov
# Fourth exercise

"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
"""

from abc import ABC, abstractmethod


class Store:
    def __init__(self, name):
        self.__name = name


class Equipment(ABC):
    def __init__(self, vendor_name):
        self._vendor_name = vendor_name

    @abstractmethod
    def show_info(self):
        pass


class Printer(Equipment):
    def __init__(self, vendor_name, device_type, paper_size, is_color):
        super().__init__(vendor_name)
        self.__type = device_type
        self.__size = paper_size
        self.__is_color = is_color

    def show_info(self):
        print(
            f"Printer of {self._vendor_name} with type {self.__type} and {self.__size} size, support color: {self.__is_color}")


class Scanner(Equipment):
    def __init__(self, vendor_name, paper_size):
        super().__init__(vendor_name)
        self.__size = paper_size

    def show_info(self):
        print(
            f"Scanner of {self._vendor_name} with {self.__size} size")


class CopyMachine(Equipment):
    def __init__(self, vendor_name, paper_size, is_auto_feed):
        super().__init__(vendor_name)
        self.__size = paper_size
        self.__is_auto_feed = is_auto_feed

    def show_info(self):
        print(
            f"CopyMachine of {self._vendor_name} with {self.__size} size and support Auto Feed: {self.__is_auto_feed}")


bw_printer = Printer("HP", "Laser", "A3", False)
bw_printer.show_info()
color_printer = Printer("Dell", "Laser", "A4", True)
color_printer.show_info()
scanner1 = Scanner("Konica", "A4")
scanner1.show_info()
copy_machine1 = CopyMachine("Xerox", "A3", True)
copy_machine1.show_info()
