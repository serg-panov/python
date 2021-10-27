# Sergey Panov
# Fifth exercise

"""
Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).
"""

from abc import ABC, abstractmethod


class Store:
    def __init__(self, name):
        self.__name = name
        self.__store_items = {}
        self.__department_items = {}

    def add_item(self, equip):
        if equip.__class__.__name__ not in self.__store_items:
            self.__store_items[equip.__class__.__name__] = [equip]
        else:
            self.__store_items[equip.__class__.__name__].append(equip)

    def show_store_items(self):
        print(f'{self.__name} items:')
        for k, v in self.__store_items.items():
            print(f"\t{k} ({len(v)})")
            for e in v:
                print("\t\t", end='')
                e.show_info()

    def move_item(self, dep, equip):
        if equip.__class__.__name__ not in self.__store_items:
            raise ValueError(f"{equip.__class__.__name__} item  not found on store {self.__name}")
        found = list(filter(lambda i: i.serial_num == equip.serial_num,
                            self.__store_items[equip.__class__.__name__]))
        if len(found) == 0:
            raise ValueError(f"Item with S/N {equip.serial_num} not found on store {self.__name}")
        # remove and assign must be do in transaction
        self.__store_items[equip.__class__.__name__].remove(found[0])
        # assign to department
        if dep not in self.__department_items:
            self.__department_items[dep] = [found[0]]
        else:
            self.__department_items[dep].append(found[0])

    def show_deps_items(self):
        for k, v in self.__department_items.items():
            print(f"Department {k} has {len(v)} items")
            for e in v:
                print("\t", end='')
                e.show_info()


class Equipment(ABC):
    def __init__(self, vendor_name, serial_num):
        self._vendor_name = vendor_name
        self._serial_num = serial_num

    @abstractmethod
    def show_info(self):
        pass

    @property
    def serial_num(self):
        return self._serial_num


class Printer(Equipment):
    def __init__(self, vendor_name, serial_num, device_type, paper_size, is_color):
        super().__init__(vendor_name, serial_num)
        self.__type = device_type
        self.__size = paper_size
        self.__is_color = is_color

    def show_info(self):
        print(
            f'{self.__class__.__name__} of {self._vendor_name} with type {self.__type} and '
            f'{self.__size} size and S/N {self.serial_num}, support color: {self.__is_color}')


class Scanner(Equipment):
    def __init__(self, vendor_name, serial_num, paper_size):
        super().__init__(vendor_name, serial_num)
        self.__size = paper_size

    def show_info(self):
        print(
            f"{self.__class__.__name__} of {self._vendor_name} and S/N {self.serial_num} with {self.__size} size")


class CopyMachine(Equipment):
    def __init__(self, vendor_name, serial_num, paper_size, is_auto_feed):
        super().__init__(vendor_name, serial_num)
        self.__size = paper_size
        self.__is_auto_feed = is_auto_feed

    def show_info(self):
        print(
            f"{self.__class__.__name__} of {self._vendor_name} and S/N {self.serial_num} with {self.__size} "
            f"size and support Auto Feed: {self.__is_auto_feed}")


store = Store("Main store")
store.add_item(Printer("HP", "123", "Laser", "A3", False))
store.add_item(Printer("Dell", "456", "Laser", "A4", True))
store.add_item(Scanner("Konica", "789", "A4"))
store.add_item(CopyMachine("Xerox", "001", "A3", True))
store.show_store_items()

store.move_item("Sales", Printer("Dell", "456", "Laser", "A4", True))
store.show_store_items()
store.show_deps_items()
# store.move_item("Sales", Printer("HP", "555", "Laser", "A3", False))
