#!/usr/bin/python3

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# ----------------------------------------------------------
class Dog:
    """Represents a dog with a name and age."""
    # Class attribute
    species = "Canis familiaris"

    # Method constructor
    def __init__(self, name, age):
        """Initializes a new Dog instance.

        Args:
            name: The name of the dog.
            age: The age of the dog.
        """
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        """Returns a string describing the dog.

        Returns:
            A string in the format "<name> is <age> years old".
        """
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        """Makes the dog speak.

        Args:
            sound: The sound the dog makes.

        Returns:
            A string in the format "<name> says <sound>".
        """
        return f"{self.name} says {sound}"

    def why(self, mytype):
        """Returns a string indicating the type of the instance.

        Args:
            mytype: The type of the instance.

        Returns:
            A string in the format "Je suis un <mytype>".
        """
        return f"Je suis un {mytype}"

class Toto1(Dog):
    """Represents a specific type of Dog called Toto1."""
    # Class attribute
    species = "Toto1 familiaris"

    def speak(self):
        """Makes Toto1 speak with a specific sound.

        Returns:
            A string indicating Toto1's bark and type.
        """
        return f"WAF toto1 / {super().why(mytype='chien toto1')}"

class Toto2(Dog):
    """Represents a specific type of Dog called Toto2."""
    # Class attribute
    species = "Toto2 familiaris"

    def speak(self):
        """Makes Toto2 speak with a specific sound.

        Returns:
            A string indicating Toto2's bark and type.
        """
        return f"WAF toto2 / {super().why(mytype='chien toto2')}"

# ----------------------------------------------------------
class Car:
    """Represents a car with a color and mileage."""
    # Class attribute
    species = "My Car class"

    # Method constructor
    def __init__(self, color, mileage):
        """Initializes a new Car instance.

        Args:
            color: The color of the car.
            mileage: The mileage of the car.
        """
        self.color = color
        self.mileage = mileage

    # Instance method
    def description(self):
        """Returns a string describing the car.

        Returns:
            A string in the format "The <color> car has <mileage> miles."
        """
        return f"The {self.color} car has {self.mileage:,} miles."
# ----------------------------------------------------------
foo1 = Toto1("foo1", 10)
foo2 = Toto2("foo2", 20)
if isinstance(foo1, Dog):
    print("foo1 est une instance de Dog")
if isinstance(foo1, Toto1):
    print("foo1 est une instance de Toto1")

print("DOG :: ------------------")
print( f"foo1: species: {foo1.species} / age: {foo1.age} / speak: {foo1.speak()}" )
print( f"foo2: species: {foo2.species} / age: {foo2.age} / speak: {foo2.speak()}" )
print( f"foo1: method description: {foo1.description()}" )
print( f"foo2: method description: {foo2.description()}" )
# ----------------------------------------------------------
print("CAR :: ------------------")
car1 = Car("blue", 20_000)
car2 = Car("red", 30_000)
for car in (car1, car2):
    print( f"{car.description()}" )
