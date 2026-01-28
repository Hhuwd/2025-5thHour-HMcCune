import random
import time


rockyDict = {
    "Mercury" : {
        "HP" : 30,
        "Init" : 4,
        "AC" : 13,
        "AtkMod": 3,
        "Damage" : random.randint(1,6) + random.randint(1,6)
    },
    "Venus" : {
        "HP" : 40,
        "Init" : 1,
        "AC" : 16,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + random.randint(1,6)
    },
    "Earth" : {
        "HP" : 41,
        "Init" : 2,
        "AC" : 15,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + random.randint(1,6)
    },
    "Mars" : {
        "HP" : 38,
        "Init" : 3,
        "AC" : 14,
        "AtkMod": 6,
        "Damage" : random.randint(1,6) + random.randint(1,6),
    }
}

gasDict = {
    "Pluto" : {
        "HP" : 25,
        "Init" : 5,
        "AC" : 10,
        "AtkMod": 1,
        "Damage" : random.randint(1,6) + random.randint(1,6)
    },
    "Neptune": {
        "HP" : 50,
        "Init": 1,
        "AC" : 17,
        "AtkMod": 5,
        "Damage" : random.randint(1,6) + random.randint(1,6)
    },
    "Uranus": {
        "HP" : 53,
        "Init": 1,
        "AC" : 14,
        "AtkMod": 6,
        "Damage" : random.randint(1,6) + random.randint(1,6)
    },
    "Saturn": {
        "HP" : 71,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,6) + random.randint(1,6)
    },
    "Jupiter": {
        "HP" : 127,
        "Init": 2,
        "AC" : 18,
        "AtkMod": 8,
        "Damage" : random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4
    },
}