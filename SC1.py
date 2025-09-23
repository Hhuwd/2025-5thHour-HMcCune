#Name: Hogan McCune
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.
damagespood = 10
damagek = 27
damageking = 5
damagems = 100
damagenuke = 100000

Roster = {
    "Spooder": {
        "Damage": damagespood,
        "Faction": "Monsters",
        "Tool": "Claws"
    },
   "EnemyKnight": {
        "Damage": damagek,
        "Faction": "Karl Imperial State",
        "Tool": "Sword"
    },
   "enemy king": {
        "Damage": damageking,
        "Faction": "Karl Imperial State",
        "Tool": "Fists"
    },
    "Mega Spooder": {
        "Damage": damagems,
        "Faction": "Monsters",
        "Tool": "Mega Claws"
    },
    "B-83 Thermonuclear Bomb": {
        "Damage": damagenuke,
        "Faction": "United States of America (Secret)",
        "Tool": "Uranium"
    },
}
print (Roster)
damagespood = int(input("Input new damage values for Spooders here:"))
Roster["Spooder"].update( {"Damage" : damagespood})
print(Roster["Spooder"]["Damage"])

damagek = int(input("Input new damage values for Knights here:"))
Roster["EnemyKnight"].update( {"Damage" : damagek})
print(Roster["EnemyKnight"]["Damage"])

damageking = int(input("Input new damage values for Kings here:"))
Roster["enemy king"].update( {"Damage" : damageking})
print(Roster["enemy king"]["Damage"])

damagems = int(input("Input new damage values for Mega Spooders here:"))
Roster["Mega Spooder"].update( {"Damage" : damagems})
print(Roster["Mega Spooder"]["Damage"])

damagenuke = int(input("Input new damage values for Nukes here:"))
Roster["B-83 Thermonuclear Bomb"].update( {"Damage" : damagenuke})
print(Roster["B-83 Thermonuclear Bomb"]["Damage"])

print (Roster)