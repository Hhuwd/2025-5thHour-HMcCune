#Name: Hogan McCune
#Class: 5th Hour
#Assignment: Semester Project 1

import random
import time

#Due to weird time travelling circumstances beyond explanation, you find yourself in 2018 or so
#working for Larian Studios. Currently, they are working on the early prototypes of the hype
#upcoming game "Baldur's Gate 3". BG3 is a game that uses the Dungeons & Dragons 5th edition rules
#as its framework for gameplay. You have been given a basic dictionary of some of the main hero
#characters and some of the enemies they may face, and are tasked with making an early prototype
#of one of the party members fighting against an enemy until one of them hits zero HP (dies).

partyDict = {
    "LaeZel" : {
        "HO" : 48,
        "Init" : 1,
        "AC" : 17,
        "AtkMod": 6,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 3
    },
    "Shadowheart" : {
        "HP" : 40,
        "Init" : 1,
        "AC" : 18,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 3,
    },
    "Gale" : {
        "HP" : 32,
        "Init" : 1,
        "AC" : 14,
        "AtkMod": 6,
        "Damage" : random.randint(1,10) + random.randint(1,10),
    },
    "Astarion" : {
        "HP" : 40,
        "Init" : 3,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,8) + random.randint(1,6) + 4,
    }
}

enemyDict = {
    "Goblin" : {
        "HP" : 7,
        "Init" : 0,
        "AC" : 12,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 2
    },
    "Orc": {
        "HP" : 15,
        "Init": 1,
        "AC" : 13,
        "AtkMod": 5,
        "Damage" : random.randint(1,12) + 3
    },
    "Troll": {
        "HP" : 84,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 4
    },
    "Mindflayer": {
        "HP" : 71,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + 4
    },
    "Dragon": {
        "HP" : 127,
        "Init": 2,
        "AC" : 18,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4
    },
}
#GALE VS DRAGON!!!
#Combat consists of these steps:

#1. Rolling for 'initiative' to see who goes first. This is determined by rolling a
#20-sided die (d20) and adding their initiative modifier (If the roll is the same,
#assume the hero goes first).
dice1 = random.randint(1,20) + (partyDict["Gale"]["Init"])
dice2 = random.randint(1,20) + (enemyDict["Dragon"]["Init"])
print("Gale rolled for turn order:", dice1)
print("Dragon rolled for turn order:", dice2)
if dice2 > dice1:
    x = "dragonfirst"
else:
    x = "galefirst"
#2. Rolling to attack. This is determined by rolling a 20-sided die (d20) and adding their
#attack modifier. The attack hits if it matches or is higher than the target's Armor Class (AC).
#If the d20 rolled to attack is an unmodified ("natural") 20, the attack automatically hits and
#the character deals double damage. If the d20 rolled to attack is an unmodified ("natural") 1,
#the attack automatically misses
if x == "dragonfirst":
    while (enemyDict["Dragon"]["HP"]) > 0 and (partyDict["Gale"]["HP"]) > 0:
        print("The Dragon Rolls to Attack!")
        time.sleep(1)
        dice2 = random.randint(1,20)
        if dice2 == 20:
            temp20 = (enemyDict["Dragon"]["Damage"]) * 2
            (partyDict["Gale"]["HP"]) = (partyDict["Gale"]["HP"]) - (enemyDict["Dragon"]["Damage"])
            time.sleep(1)
            print("CRITICAL HIT! Gale's New HP:", (partyDict["Gale"]["HP"]))
        elif dice2 == 1:
            print("HAHA! THE DRAGON GOT A ONE!!! MISSED!!!")
        else:
            dice2 = dice2 + (enemyDict["Dragon"]["AtkMod"])
            if dice2 > (partyDict["Gale"]["AC"]):
                (partyDict["Gale"]["HP"]) = (partyDict["Gale"]["HP"]) - (enemyDict["Dragon"]["Damage"])
                time.sleep(1)
                print("The Dragon hits!")
                print("Gale's New HP:", (partyDict["Gale"]["HP"]))
            else:
                time.sleep(1)
                print("The Dragon misses!")
        print("Gale Rolls to Attack!")
        time.sleep(1)
        dice2 = random.randint(1,20)
        if dice2 == 20:
            temp20 = (partyDict["Gale"]["Damage"]) * 2
            (enemyDict["Dragon"]["HP"]) = (enemyDict["Dragon"]["HP"]) - (partyDict["Gale"]["Damage"])
            time.sleep(1)
            print("CRITICAL HIT! The Dragon's New HP:", (enemyDict["Dragon"]["HP"]))
        elif dice2 == 1:
            print("HAHA! GALE GOT A ONE!!! MISSED!!!")
        else:
            dice2 = dice2 + (partyDict["Gale"]["AtkMod"])
            if dice2 > (enemyDict["Dragon"]["AC"]):
                (enemyDict["Dragon"]["HP"]) = (enemyDict["Dragon"]["HP"]) - (partyDict["Gale"]["Damage"])
                time.sleep(1)
                print("Gale hits!")
                print("The Dragon's New HP:", (enemyDict["Dragon"]["HP"]))
            else:
                time.sleep(1)
                print("Gale misses!")
else:
    while (enemyDict["Dragon"]["HP"]) > 0 and (partyDict["Gale"]["HP"]) > 0:
        print("Gale Rolls to Attack!")
        time.sleep(1)
        dice2 = random.randint(1, 20)
        if dice2 == 20:
            temp20 = (partyDict["Gale"]["Damage"]) * 2
            (enemyDict["Dragon"]["HP"]) = (enemyDict["Dragon"]["HP"]) - (partyDict["Gale"]["Damage"])
            time.sleep(1)
            print("CRITICAL HIT! The Dragon's New HP:", (enemyDict["Dragon"]["HP"]))
        elif dice2 == 1:
            print("HAHA! GALE GOT A ONE!!! MISSED!!!")
        else:
            dice2 = dice2 + (partyDict["Gale"]["AtkMod"])
            if dice2 > (enemyDict["Dragon"]["AC"]):
                (enemyDict["Dragon"]["HP"]) = (enemyDict["Dragon"]["HP"]) - (partyDict["Gale"]["Damage"])
                time.sleep(1)
                print("Gale hits!")
                print("The Dragon's New HP:", (enemyDict["Dragon"]["HP"]))
            else:
                time.sleep(1)
                print("Gale misses!")
            print("The Dragon Rolls to Attack!")
            time.sleep(1)
            dice2 = random.randint(1,20)
            if dice2 == 20:
                temp20 = (enemyDict["Dragon"]["Damage"]) * 2
                (partyDict["Gale"]["HP"]) = (partyDict["Gale"]["HP"]) - (enemyDict["Dragon"]["Damage"])
                time.sleep(1)
                print("CRITICAL HIT! Gale's New HP:", (partyDict["Gale"]["HP"]))
            elif dice2 == 1:
                print("HAHA! THE DRAGON GOT A ONE!!! MISSED!!!")
            else:
                dice2 = dice2 + (enemyDict["Dragon"]["AtkMod"])
                if dice2 > (partyDict["Gale"]["AC"]):
                    (partyDict["Gale"]["HP"]) = (partyDict["Gale"]["HP"]) - (enemyDict["Dragon"]["Damage"])
                    time.sleep(1)
                    print("The Dragon hits!")
                    print("Gale's New HP:", (partyDict["Gale"]["HP"]))
                else:
                    time.sleep(1)
                    print("The Dragon misses!")
#3. If the attack hits, roll damage and subtract it from the target's hit points.

#4. The second in initiative rolls to attack (and rolls damage) afterwards.

#5. Repeat steps 2-5 until one of the characters is dead.