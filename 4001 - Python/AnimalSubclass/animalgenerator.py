#Animal Generator

import Animal
from Animal import Mammal
from Animal import Bird

animals = list()

print("Hello, welcome to the Animal Generator!")
print("This program uses classes to create animals!\n")

while True:
    print("Would you like to create a mammal or bird?")
    print("1. Mammal")
    print("2. Bird")
    choice = int(input("Which would you like to create? "))
    if (choice == 1):
        MSpecies = input("What type of Mammal would you like to create? ")
        MName = input("What is the mammal's name? ")
        MColor = input("What color is the mammal's hair? ")
        print("\n")
        animal = Animal.Mammal(MSpecies, MName, MColor)
        animals.append( animal )

    elif (choice == 2):
        BSpecies = input("What type of Bird would you like to create? ")
        BName = input("What is the bird's name? ")
        BFly = input("Can the bird fly? ")
        print("\n")
        animal = Animal.Bird(BSpecies, BName, BFly)
        animals.append( animal )

    choice = input("Would you like to create more animals? (y/n)")
    if choice != 'y':
        break

print("Your animals are:\n")

for animal in animals:
    animalN = animal.getName()
    animalT = animal.get_animalType()
    animalM = animal.getMood()

    print(animalN, "the", animalT,"is", animalM)
