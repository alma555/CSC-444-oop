class Duck():
    def __init__(self):
        self.name = str
        self.age = int
        self.ponds = list
    
    def swim(self):
        print("splish splash splish splash")
    
    def quack(self):
        print("quaaaaaack")

    def check_pond_water(self, Pond):
        if Pond.pollution_concentration >= 0.1:
            return False
        if Pond.vegetation <= 0.05:
            return False
        else: return True

    def add_pond(self, Pond):
        if self.check_pond_water(Pond) == True:
            self.ponds.append(Pond)
        else: print("failed to ensure pond safety")

class Pond():
    def __init__(self):
        self.pollution_concentration = float(1000000)
        self.vegetation = float(-10000)

def test():
    mr_waddles = Duck()
    pond = Pond()
    mr_waddles.swim()
    mr_waddles.quack()
    mr_waddles.add_pond(pond)
    
test()
