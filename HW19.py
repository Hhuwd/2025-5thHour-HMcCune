#Name:
#Class: 5th Hour
#Assignment: HW19

#1. Import the def functions created in problem 1-4 from HW16
from HW16 import yes, amogus, ma, loop
#2. Call the functions here and run HW19
yes()
amogus(2,3,4)
ma("Penguin","Bird","Dog","Cat","Elephant")
loop(15)
#3. Delete all calls from HW15 and run HW19 again.
#done
#4. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("Hello World!")
#5. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    d = int(input("Enter a number:"))
    y = 100 / d
    print(y)
except ZeroDivisionError:
    print("DIVIDED BY ZERO???? I CAN'T COMPUTE THAT!")
#6. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    p = int(input("Enter a number:"))
    print(p)
except ValueError:
    print("NOT AN INTEGER!")
#7. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
j = 5
while j > 0:
    print(j)
    j -= 1
    if j <= 0:
        raise Exception("ZERO!!!!!!")
