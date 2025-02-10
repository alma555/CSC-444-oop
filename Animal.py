from abc import ABC, abstractmethod

#submission from: Michael, working with Alma and Selase

class Animal(ABC):
    def __init__(self):
        self.name = str
        self.species = str
        self.age = int

    #getter
    @property
    def age(self):
        return self._age

    #setter
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be a negative number.")
        self._age = value

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Wolf(Animal):
    def __init__(self):
        self.name = "Julian"
        self.age = 7
        self.species = "Canis Lupus Lupus"

    def make_sound(self):
        print("Grrrowll")
    
    def move(self):
        print("The wolf walks quiety around the enclosure")

class RedPanda(Animal):
    def __init__(self):
        self.name = "Audrey"
        self.age = 21
        self.species = "Ailurus fulgens"

    def make_sound(self):
        print("The red panda is not a noisy animal! It sits silently in the branches of a tree.")

    def move(self):
        print("The hungry red panda shovels bamboo into its mouth")

class mouse(Animal):

    def __init__(self):
        self.name = "Mr Mouse"
        self.age= 3
        self.species = "Rodent"

    def move(self):
        print( "The mouse is walking")

    def make_sound(self):
        print ("sqeak!!!")

class Crab(Animal):
    def __init__(self):
        self.name = "Crabby"
        self.age = 1
        self.species = "Crustacean"

    def move(self):
        print("The crab is burrowing")

    def make_sound(self):
        print("Click!!!")



