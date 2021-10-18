# Sergey Panov
# First exercise

"""
Создать класс TrafficLight (светофор).
- определить у него один атрибут color (цвет) и метод running (запуск);
- атрибут реализовать как приватный;
- в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
- продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
- переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
- проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""


class TrafficLight:
    def __init__(self):
        self.__color = "Yellow"
        self.__sequence = {"Red": [{"Yellow"}, 7], "Yellow": [{"Green", "Red"}, 2], "Green": [{"Yellow"}, 5]}
        self.running("Red")

    def running(self, color):
        if not self.__sequence.get(color):
            raise ValueError('Invalid color')
        if self.__color == color:
            raise ValueError(f'{color} already switched on')
        if color not in self.__sequence.get(self.__color)[0]:
            raise ValueError(f'Unexpected color {color} for current mode')
        print(f"Switch on {color} during {self.__sequence.get(color)[1]} seconds")
        self.__color = color


tl = TrafficLight()
tl.running("Yellow")
# tl.running("Yellow")  # exception 'already switched on'
tl.running("Green")
# tl.running("Red")  # exception 'Unexpected color {color} for current mode'
tl.running("Yellow")
tl.running("Red")
# tl.running("White")  # exception 'Invalid color'
