#Name: Hogan McCune
#Class: 5th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def ten():
    print("Hello World!")
#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
i = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def eleven():
    global heads, tails, i
    while i < 100:
        coin_flip_result = random.randint(1, 2)
        if coin_flip_result == 1:
            heads += 1
            i = i + 1
        else:
            tails += 1
            i = i + 1
#4. Call the "Hello world" and "Coin Flip" functions here
ten()
eleven()
#5. Print the final result of heads and tails here
print(heads, tails)
#6. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["Blue", "Green", "White", "Red", "Orange"]
#7. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def twelve():
    global beanBag
    if beanBag == []:
        print("BeanBag is empty!")
    else:
        hand = (random.choice(beanBag))
        print(hand)
        beanBag.remove(hand)
        yed()
#8. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def yed():
    e = (input("Would you like to pull another bean out? (y/n) "))
    if e == "y":
        twelve()
    else:
        print("Thank you for playing!")
#9. Call the "Bean Pull" function here
twelve()