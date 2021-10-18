# Sergey Panov
# Third exercise

"""
Реализовать базовый класс Worker (работник).
- определить атрибуты: name, surname, position (должность), income (доход);
- последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
- создать класс Position (должность) на базе класса Worker;
- в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
- проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name, surname, position, income_wage, income_bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": income_wage, "bonus": income_bonus}


class Position(Worker):
    def __init__(self, name, surname, position, income_wage, income_bonus):
        super().__init__(name, surname, position, income_wage, income_bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


pos1 = Position('Ivan', 'Ivanov', 'Manager', 50000, 15000)
pos2 = Position('Petr', 'Petrov', 'CEO', 100000, 30000)
print(f'Full name: {pos1.get_full_name()}, Total income: {pos1.get_total_income()}')
print(f'Full name: {pos2.get_full_name()}, Total income: {pos2.get_total_income()}')
