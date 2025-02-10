from Animal import Animal, Wolf, RedPanda 
from mouse import mouse
from Crab import Crab
from Zebra import Zebra

#submission from: Alma, working with Selase & Michael

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def visit(self):
        for animal in self.animals:
            animal.make_sound()
            animal.move()
        print("you visited the zoo; come back soon!")

def test_zoo():
    zoo = Zoo()
    animal_shipment = [mouse(), Crab(), Wolf(), RedPanda(), Zebra()]
    for animal in animal_shipment:
        zoo.add_animal(animal)
    zoo.visit()

test_zoo()
