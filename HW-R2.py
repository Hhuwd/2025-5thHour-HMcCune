#Name: Hogan McCune
#Class: 5th Hour
#Assignment: HW-R2


#1. Print "Hello World!"
print("Hello World!")
#2. Create an empty list.
x = []
#3. Create a list that contains the names of everyone in the classroom.
y = ["Ashton","Bryson","Aiden","Sam","Hogan","Ivan","Dylan"]
#4. Print the list from #3, sort the list, then print the list again.
print(y)
y.sort()
print(y)
#5. Append 5 different integers into the empty list from #2 and print the list.
x.append(9)
x.append(4)
x.append(3)
x.append(2)
x.append(100)
print(x)
#6. Add together the middle three numbers in the list from #2 and print the result.
print(x[1] + x[2] + x[3])
#7. Remove the very first number in the list from #2. Print the new first number.
x.pop(0)
print(x[0])
#8. Create a dictionary with three keys with respective values: your name, your grade, and your favorite color.
me = {
    "name" : "Hogan",
    "grade" : "10",
    "color" : "Blue"
}
#9. Using the update function, add a fourth key and value determining your favorite candy.
me.update({"candy" : "Starburst"})
#10. Print ONLY the values of the dictionary from #8.
print(me.values())