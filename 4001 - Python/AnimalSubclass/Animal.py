#Defining class Animal

import random

class Animal:
    def __init__(self, animalType, Name):
        self.__animalType = animalType
        self.__name = Name

        randomNum = random.randint(1,3)

        if randomNum == 1:
            self.__mood = "happy"
        elif randomNum == 2:
            self.__mood = "hungry"
        elif randomNum == 3:
            self.__mood = "sleepy"

    def get_animalType( self ):
        return self.__animalType

    def getName( self ):
        return self.__name

    def getMood( self ):
        return self.__mood

class Mammal( Animal ):
    def __init__(self, animalType, Name, haircolor):
        super().__init__(animalType, Name)
        self.__hair_color = haircolor

    def get_hair_color( self ):
        return self.__hair_color

class Bird( Animal ):
    def __init__(self, animalType, Name, Fly):
        super().__init__(animalType, Name)
        self.__can_fly = Fly

    def get_can_fly( self ):
        return self.__can_fly

        
