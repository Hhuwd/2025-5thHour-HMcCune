#Name: Hogan McCune
#Class: 5th Hour
#Assignment: HW10
from operator import truediv
import math

#1. Print Hello World!
print("Hello World!")
#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login = True
admin = True
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
numA = 0
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi == True:
    if login == True:
        if admin == True:
            print("Welcome to Wifi!")
            numA = numA + 1
            print(numA)
        else:
            print("ERROR: YOU DO NOT HAVE ADMIN!")
    else:
        print("ERROR: YOU DO NOT HAVE LOGIN CREDINTIALS!")
else:
    print("ERROR: YOU DO NOT HAVE WIFI!")