class Vehicle:
    def __init__(self, brand, speed, fuel):
        self.brand = brand
        self.speed = speed
        self.fuel = fuel

    def move(self):
        return f"{self.brand} is moving at {self.speed} km/h"

    def refuel(self):
        return f"{self.brand} is refueling with {self.fuel}"

    def __str__(self):
        return f"Vehicle: {self.brand}, Speed: {self.speed} km/h, Fuel: {self.fuel}"


class Car(Vehicle):
    def __init__(self, brand, speed, fuel, doors):
        super().__init__(brand, speed, fuel)
        self.doors = doors

    def move(self):
        return f"Car {self.brand} is driving at {self.speed} km/h with {self.doors} doors"

    def honk(self):
        return f"{self.brand}: Beep beep!"

    def __str__(self):
        return f"Car: {self.brand}, Speed: {self.speed} km/h, Doors: {self.doors}"


class Motorcycle(Vehicle):
    def __init__(self, brand, speed, fuel, type):
        super().__init__(brand, speed, fuel)
        self.type = type

    def move(self):
        return f"Motorcycle {self.brand} is riding at {self.speed} km/h"

    def wheelie(self):
        return f"{self.brand} is doing a wheelie!"

    def __str__(self):
        return f"Motorcycle: {self.brand}, Speed: {self.speed} km/h, Type: {self.type}"
