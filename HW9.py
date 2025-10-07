#Name: Hogan McCune
#Class: 6th Hour
#Assignment: HW9

import random

#1. Print "Hello World!"
print("Hello World!")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
a = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
#3. Print the list.
print (a)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if a[0]>a[1] and a[0]>a[2]:
    print(a[0],"Is the biggest!")
elif a[1]>a[0] and a[1]>a[2]:
    print(a[1],"Is the biggest!")
elif a[2]>a[0] and a[2]>a[1]:
    print(a[2],"Is the biggest!")
else:
    print("Some numbers are equal! There is no biggest number!")
#5. Tie the result (the largest number) from #4 to a variable called "num".
if a[0]>a[1] and a[0]>a[2]:
    num = a[0]
elif a[1]>a[0] and a[1]>a[2]:
    num = a[1]
elif a[2]>a[0] and a[2]>a[1]:
    num = a[2]
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print(num, "is divisible by both 2 and 3!")
    else: print(num, "is divisible by 2, but not 3!")
elif num % 3 == 0:
    if num % 2 == 0:
        print(num, "is divisible by both 2 and 3!")
    else: print(num, "is divisible by 3, but not 2!")
else: print(num, "Is not divisible by either 2 or 3!")