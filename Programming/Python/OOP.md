# OOP (Object Oriented Programming) in Python
In this example, the Car class has attributes like make, model, year, color, and is_running. 
It also has methods like start_engine, stop_engine, and honk to perform actions related to the car.


``` Python

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            print(f"The {self.color} {self.year} {self.make} {self.model}'s engine is starting.")
            self.is_running = True
        else:
            print("The engine is already running.")

    def stop_engine(self):
        if self.is_running:
            print(f"The {self.color} {self.year} {self.make} {self.model}'s engine is stopping.")
            self.is_running = False
        else:
            print("The engine is already stopped.")

    def honk(self):
        print(f"The {self.color} {self.year} {self.make} {self.model} is honking!")

# Creating an instance of the Car class
my_car = Car(make="Toyota", model="Camry", year=2022, color="Blue")

# Accessing attributes
print(f"My car is a {my_car.year} {my_car.color} {my_car.make} {my_car.model}.")

# Calling methods
my_car.start_engine()
my_car.honk()
my_car.stop_engine()

```








