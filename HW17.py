#Name: Hogan McCune
#Class: 5th Hour
#Assignment: HW17
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def yes():
    b = random.randint(1, 3)
    a = int(input("Hello! Welcome to Rock, Paper, Scissors! input 1 for rock, 2 for paper, 3 for scissors!"))
    if a == 1:
        if b == 1:
            print("You both picked rock!")
        elif b == 2:
            print("Opponent picked paper! YOU LOSE!")
        else:
            print("Opponent picked scissors! YOU WIN!")
        ten()
    elif a == 2:
        if b == 1:
            print("Opponent picked Rock! YOU WIN!")
        elif b == 2:
            print("You both picked paper!")
        else:
            print("Opponent picked scissors! YOU LOSE!")
        ten()
    elif a == 3:
        if b == 1:
            print("Opponent picked Rock! YOU LOSE!")
        elif b == 2:
            print("Opponent picked paper! YOU WIN!")
        else:
            print("You both picked scissors!")
        ten()
    else:
        print("You didnt pick anything!")
        yes()
#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def ten():
    e = (input("Would you like to play again? (y/n) "))
    if e == "y":
        yes()
    else:
        print("Thank you for playing!")

yes()