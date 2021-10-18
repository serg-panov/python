# Sergey Panov
# Fourth exercise

"""
Реализуйте базовый класс Car.
- у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
- опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
- добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
- для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f"Go with {speed} km/h")

    def stop(self):
        self.speed = 0
        print("Stop!")

    def turn(self, direction):
        print(f"Turn to the {direction}")

    def show_speed(self):
        print(f"Current speed for {self.name} of {self.color} color is {self.speed}")


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Current speed for {self.name} of {self.color} color is {self.speed}, OVER SPEED!!!")
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Current speed for {self.name} of {self.color} color is {self.speed}, OVER SPEED!!!")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


car1 = TownCar("Green", "Mazda")
print(f"car1 is {car1.name} of {car1.color} color, is police? {car1.is_police}")
car1.show_speed()
car1.go(40)
car1.show_speed()
car1.turn("Left")
car1.go(70)
car1.show_speed()
car1.stop()

car2 = SportCar("Red", "Mercedes")
print(f"car2 is {car2.name} of {car2.color} color, is police? {car2.is_police}")
car2.show_speed()
car2.go(40)
car2.show_speed()
car2.turn("Left")
car2.go(170)
car2.show_speed()
car2.stop()

car3 = WorkCar("Yellow", "Kia")
print(f"car3 is {car3.name} of {car3.color} color, is police? {car3.is_police}")
car3.show_speed()
car3.go(40)
car3.show_speed()
car3.turn("Left")
car3.go(41)
car3.show_speed()
car3.stop()

car4 = PoliceCar("Blue", "BMW")
print(f"car4 is {car4.name} of {car4.color} color, is police? {car4.is_police}")
car4.show_speed()
car4.go(40)
car4.show_speed()
car4.turn("Right")
car4.go(200)
car4.show_speed()
car4.stop()
