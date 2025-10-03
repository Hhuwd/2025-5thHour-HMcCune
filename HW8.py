#Name: Hogan McCune
#Class: 5th Hour
#Assignment: HW8

import random

#1. Print "Hello World!"
print("Hello World!")
#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
#3. Print A, B, and C on the same line.
print(a,b,c)
#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.
if a > 5:
    print("A is greater than 5")
elif a < 5:
    print("A is less than 5")
elif a == 5:
    print("A is equal to 5")
#5. Make an if statement that prints if variable B is between 3 and 7, or not.
if b > 3 and b < 7:
    print("B is between 3 or 7!")
else:
    print("B is NOT between 3 or 7!")
#6. Make an if statement that prints if variable C is even or odd.
if c % 2 == 0:
    print(f"{c} is even")
else:
    print(f"{c} is odd")
#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20
d = 3 + random.randint(1,20)
#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.
sum = a + b + c
if sum > d:
    print("ABC is greater than D")
elif sum < d:
    print("ABC is less than D")
elif sum == d:
    print("ABC is equal to D")