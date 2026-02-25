#Name: Hogan McCune
#Class: 5th Hour
#Assignment: Scenario 6

import random
import time

#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Semester Project 1 using classes instead of dictionaries, include and refactor
#the combat test code below as well.)

#Classes and stuff
class character:
    def __init__(self, HP, Init, AC, AtkMod, Damage):
        self.HP = HP
        self.Init = Init
        self.AC = AC
        self.AtkMod = AtkMod
        self.Damage = Damage

class enemy:
    def __init__(self, HP, Init, AC, AtkMod, Damage):
        self.HP = HP
        self.Init = Init
        self.AC = AC
        self.AtkMod = AtkMod
        self.Damage = Damage

#Characters (Party):
LaeZel = character(48, 1, 17, 6, random.randint(1,6) + random.randint(1,6) + 3)
Shadowheart = character(40, 1, 18, 4, random.randint(1,6) + 3)
Gale = character(32, 1, 17, 6, random.randint(1,10) + random.randint(1,10))
Astarion = character(40, 3, 17, 5, random.randint(1,8) + random.randint(1,6) + 4)

#Characters (Enemy):
Goblin = character(7, 0, 12, 4, random.randint(1,6) + 2)
Orc = character(15, 1, 13, 5, random.randint(1,12) + 3)
Troll = character(84, 1, 15, 7, random.randint(1,6) + random.randint(1,6) + 4)
Mindflayer = character(71, 1, 15, 7, random.randint(1,10) + random.randint(1,10) + 4)
Dragon = character(127, 2, 28, 7, random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4)

#Combat Test Code (init roll)
dice1 = random.randint(1,20) + Gale.Init
dice2 = random.randint(1,20) + Dragon.Init
print("Gale rolled for turn order:", dice1)
print("Dragon rolled for turn order:", dice2)
if dice2 > dice1:
    x = "dragonfirst"
else:
    x = "galefirst"

#Combat Test Code (Main Stuff)
if x == "dragonfirst":
    while Dragon.HP > 0 and Gale.HP > 0:
        print("The Dragon Rolls to Attack!")
        time.sleep(1)
        dice2 = random.randint(1,20)
        if dice2 == 20:
            temp20 = Dragon.Damage * 2
            Gale.HP = Gale.HP - Dragon.Damage
            time.sleep(1)
            print("CRITICAL HIT! Gale's New HP:", Gale.HP)
        elif dice2 == 1:
            print("HAHA! THE DRAGON GOT A ONE!!! MISSED!!!")
        else:
            dice2 = dice2 + Dragon.AtkMod
            if dice2 > Gale.AC:
                Gale.HP = Gale.HP - Dragon.Damage
                time.sleep(1)
                print("The Dragon hits!")
                print("Gale's New HP:", Gale.HP)
            else:
                time.sleep(1)
                print("The Dragon misses!")
        print("Gale Rolls to Attack!")
        time.sleep(1)
        dice2 = random.randint(1,20)
        if dice2 == 20:
            temp20 = Gale.Damage * 2
            Dragon.HP = Dragon.HP - Gale.Damage
            time.sleep(1)
            print("CRITICAL HIT! The Dragon's New HP:", Dragon.HP)
        elif dice2 == 1:
            print("HAHA! GALE GOT A ONE!!! MISSED!!!")
        else:
            dice2 = dice2 + Gale.AtkMod
            if dice2 > Dragon.AC:
                Dragon.HP = Dragon.HP - Gale.Damage
                time.sleep(1)
                print("Gale hits!")
                print("The Dragon's New HP:", Dragon.HP)
            else:
                time.sleep(1)
                print("Gale misses!")
else:
    while Dragon.HP > 0 and Gale.HP > 0:
        print("Gale Rolls to Attack!")
        time.sleep(1)
        dice2 = random.randint(1, 20)
        if dice2 == 20:
            temp20 = Gale.Damage * 2
            Dragon.HP = Dragon.HP - Gale.Damage
            time.sleep(1)
            print("CRITICAL HIT! The Dragon's New HP:", Dragon.HP)
        elif dice2 == 1:
            print("HAHA! GALE GOT A ONE!!! MISSED!!!")
        else:
            dice2 = dice2 + Gale.AtkMod
            if dice2 > Dragon.AC:
                Dragon.HP = Dragon.HP - Gale.Damage
                time.sleep(1)
                print("Gale hits!")
                print("The Dragon's New HP:", Dragon.HP)
            else:
                time.sleep(1)
                print("Gale misses!")
            print("The Dragon Rolls to Attack!")
            time.sleep(1)
            dice2 = random.randint(1,20)
            if dice2 == 20:
                temp20 = Dragon.Damage * 2
                Gale.HP = Gale.HP - Dragon.Damage
                time.sleep(1)
                print("CRITICAL HIT! Gale's New HP:", Gale.HP)
            elif dice2 == 1:
                print("HAHA! THE DRAGON GOT A ONE!!! MISSED!!!")
            else:
                dice2 = dice2 + Dragon.AtkMod
                if dice2 > Gale.AC:
                    Gale.HP = Gale.HP - Dragon.Damage
                    time.sleep(1)
                    print("The Dragon hits!")
                    print("Gale's New HP:", Gale.HP)
                else:
                    time.sleep(1)
                    print("The Dragon misses!")