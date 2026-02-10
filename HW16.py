#Name: Hogan McCune
#Class: 5th Hour
#Assignment: HW16

import random

#1. Create a def function that prints out "Hello World!"
def yes():
    print("Hello World!")
#2. Create a def function that calculates the average of three numbers (set the 3 numbers as your arguments).
def amogus(a,b,c):
    d = (a + b + c) / 3
    print(d)
#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def ma(*leui):
    print(leui[2])
#4. Create a def function that loops from 1 to the number put in the argument.
def loop(inpu):
    for i in range(1,inpu + 1):
        print(i)
#5. Call all of the functions created in 1 - 4 with relevant arguments.

#6. Create a variable x that has the value of 2. Print x
x = 2
print(x)
#7. Create a def function that multiplies the value of 2 by a random number between 1 and 5.
def it():
    global x
    r = random.randint(1,5)
    x = x * r
it()
#8. Print the new value of x.
print(x)