import random


class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False

    def __init__(self, name, color, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f"{self.name} go!")

    def stop(self):
        print(f"{self.name} stop!")

    def turn(self):
        print(f"Name - {self.name} turn {'left' if random.randint(0, 100) > 50 else 'right'}!")

    def get_description(self):
        print(f"Name - {self.name}, Color - {self.color}, {'police car' if self.is_police else 'non police car'}")

    def show_speed(self):
        self.speed = random.randint(0, 100)
        print(f"Name - {self.name} speed is {self.speed}")


class TownCar(Car):
    def show_speed(self):
        self.speed = random.randint(0, 100)
        print(
            f"Name - {self.name} {'speed is '+str(self.speed) if self.speed<=60 else 'over speed '+str(self.speed)} ")


class SportCar(Car):
    def car_type(self):
        print("Sport car")


class WorkCar(Car):
    def show_speed(self):
        self.speed = random.randint(0, 100)
        print(
            f"Name - {self.name} {'speed is '+str(self.speed) if self.speed<=40 else 'over speed ' + str(self.speed)} ")


class PoliceCar(Car):
    def car_type(self):
        print("Police car")


t = TownCar("Chrysler", "Blue", False)
t.get_description()
t.turn()
t.show_speed()

print(5 * "*")

p = PoliceCar("Ford", "White", True)
p.get_description()
p.turn()
p.show_speed()

print(5 * "*")

w = WorkCar("Kamatsu", "Orange", False)
w.get_description()
w.turn()
w.show_speed()

print(5 * "*")

s = SportCar("Lamborgini", "Orange", False)
s.get_description()
s.turn()
s.show_speed()
