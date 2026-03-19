from models import Vehicle, Car, Motorcycle

vehicle = Vehicle("Generic", 100, "Diesel")
car = Car("Toyota", 180, "Petrol", 4)
moto = Motorcycle("Honda", 200, "Petrol", "Sport")

vehicles = [vehicle, car, moto]

for v in vehicles:
    print(v)
    print(v.move())
    print()

print("--- Polymorphism ---")
for v in vehicles:
    print(v.move())

print()
print(car.honk())
print(moto.wheelie())


## Vehicle Class Hierarchy

#Vehicle - base class with brand, speed, fuel
#Car - inherits Vehicle, adds doors attribute
#Motorcycle - inherits Vehicle, adds type attribute



















