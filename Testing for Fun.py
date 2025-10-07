#choice game





print ("Hello! welcome to choice game! There will always be 2 options, 'yes' or 'no', Would you like to begin?")
a = input()
if a == "yes":
    print("Let the games begin!")
elif a == "no":
    print("Alright then, goodbye!")
else :
    print("Sorry, I don't understand you.")
if a == "yes":
    print("You are walking in a hallway when you hear a loud noise behind you. Would you like to check the noise?")
    a = input()
    if a == "yes":
        print("You see a monster. You die. Obviously.")
    elif a == "no":
        print("You run away instead, just barely reaching your bedroom before whatever is behind you can capture you.")
    else:
        print("Sorry, I don't understand you.")
    if a == "no":
        print("YOU WIN!!!")