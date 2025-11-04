#Name: Hogan McCune
#Class: 5th Hour
#Assignment: HW12

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
import time
import random
j = 5
while j >= 0:
    print(j)
    time.sleep(1)
    j -= 1
else:
    print("Hello World!")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
b = 1
while b <= 30:
    if b % 2 == 0:
        print(b)
    b += 1
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
c = 1
while c <= 30:
    if c % 3 == 0:
        c += 1
        continue
    print(c)
    c += 1
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
a = random.randint(1,6)
while a > 1:
    print (a)
    a = random.randint(1,6)
else:
    print(a)
#5. Create a while loop that asks for a number input until the user inputs the number 0.
t = int(input("Press 0 to exit"))
while t != 0:
    t = int(input("Press 0 to exit"))