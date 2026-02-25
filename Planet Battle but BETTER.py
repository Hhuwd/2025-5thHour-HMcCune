import random
class Planets:
    def __init__(self, attack, armor, HP):
        self.attack = attack
        self.armor = armor
        self.HP = HP
    def arizona(self):
        print("arizona")

Mercury = Planets(random.randint(1,5), 1, 100)
Venus = Planets(random.randint(1,10), 3, 100)
Earth = Planets(random.randint(1,10), 2, 100)
Moon = Planets(random.randint(1,4), 1, 100)
Mars = Planets(random.randint(1,9), 2, 100)
