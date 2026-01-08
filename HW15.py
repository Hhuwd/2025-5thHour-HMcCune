#Name: Hogan McCune
#Class: 5th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
#4. Add a and b together, then divide the sum by c. Print the result.
d = a + b
e = d / c
print(e)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
round(e)
if e % 2 == 0:
    print("It's even!")
else:
    print("It's odd!")
#6. Create a list of five different random integers between 1 and 10.
list = [random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)]
#7. Print the 4th number in the list.
print(list[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
list.append(random.randint(1,10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
list.sort()
print(list[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
print(i)
while i < 100:
    i = i + i
    print(i)
#11. Create a list containing the names of five other students in the classroom.
list2 = ["Sam","Bryson","Aiden","Jude","Ashton"]
#12. Create a for loop that individually prints out the names of each student in the list.
for x in list2:
    print(x)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for i2 in range(1,101 + 1):
    print(i2)
    if i2 % 10 == 0:
        break
#14. Free space. Do something creative. :)
x = input("Would you like to begin pain?")
if x == "no":
    print("Goodbye!")
else:
    x = random.randint(1,10000)
    while x:
        print(x)
        x = random.randint(1, 10000)