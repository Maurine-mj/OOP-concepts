'''
Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.

Activity 2: Polymorphism Challenge! 🎭
Create a program that includes animals or vehicles with the same action (like move()). However,
make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while
Plane.move() prints "Flying" ✈️).
'''

#Assignment one
# Base class
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.__level = level  # Encapsulated attribute

    def introduce(self):
        print(f"I am {self.name}, and I can {self.power}!")

    def get_level(self):  # Encapsulation: getter method
        return self.__level

    def fight(self):
        print(f"{self.name} is fighting with {self.power}!")

        
class IceHero(Superhero):
    def __init__(self, name, level):
        super().__init__(name, "freeze enemies", level)

    # Polymorphism: overrides the fight method
    def fight(self):
        print(f"{self.name} launches an icy blast!")

class FireHero(Superhero):
    def __init__(self, name, level):
        super().__init__(name, "burn enemies", level)

    def fight(self):
        print(f"{self.name} throws fireballs!")

hero1 = IceHero("Frostbite", 5)
hero2 = FireHero("Blazeman", 7)

hero1.introduce()
hero1.fight()
print("Level:", hero1.get_level())

print()

hero2.introduce()
hero2.fight()
print("Level:", hero2.get_level())
print('')


#Assignment two
class Car:
    def move(self):
        print("I'm a car I move by Driving")

class plane:
    def move(self):
        print("I'm a plane I move by Flying")

class ship:
    def move(self):
        print("I'm a ship I move by sailing")

class bike:
    def move(self):
        print("I'm a bike I move by riding")

for vehicle in[Car(), plane(), ship(), bike()]:
    vehicle.move()
        



        

    
    
