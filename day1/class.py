#!/usr/bin/python3

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# ----------------------------------------------------------
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Method constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    def why(self, mytype):
        return f"Je suis un {mytype}"

class Toto1(Dog):
    # Class attribute
    species = "Toto1 familiaris"

    def speak(self):
        return "WAF toto1 / {}".format(super().why(mytype='chien toto1'))

class Toto2(Dog):
    # Class attribute
    species = "Toto2 familiaris"

    def speak(self):
        return "WAF toto2 / {}".format(super().why('chien toto2'))

# ----------------------------------------------------------
class Car:
    # Class attribute
    species = "My Car class"

    # Method constructor
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # Instance method
    def description(self):
        return f"The {self.color} car has {self.mileage:,} miles."
# ----------------------------------------------------------
foo1 = Toto1("foo1", 10)
foo2 = Toto2("foo2", 20)
if isinstance(foo1, Dog):
    print("foo1 est une instance de Dog")
if isinstance(foo1, Toto1):
    print("foo1 est une instance de Toto1")

print("DOG :: ------------------")
print( "foo1: species: {} / age: {} / speak: {}".format(foo1.species,foo1.age,foo1.speak()) )
print( "foo2: species: {} / age: {} / speak: {}".format(foo2.species,foo2.age,foo2.speak()) )
print( "foo1: method description: {}".format(foo1.description()) )
print( "foo2: method description: {}".format(foo2.description()) )
# ----------------------------------------------------------
print("CAR :: ------------------")
car1 = Car("blue", 20_000)
car2 = Car("red", 30_000)
for car in (car1, car2):
    print( "{}".format(car.description()) )


exit(0)
