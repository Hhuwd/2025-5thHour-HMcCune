#Name: Hogan McCune
#Class: 5th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
h = [10,4,6,2,346,34,3,5,1]
#2. Sort the list from highest to lowest.
h.sort(reverse=True)
#3. Create an empty list.
m = []
#4. Remove the median number from the first list and add it to the second list.
test2 = h[4]
h.pop(4)
m.append (test2)
#5. Remove the first number from the first list and add it to the second list.
test = h[0]
h.pop(0)
m.append (test)
#6. Print both lists.
print (m)
print (h)
#7. Add the two numbers in the second list together and print the result.
sum1 = m[0] + m[1]
print (sum1)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
m.pop(1)
m.pop(0)
h.append(sum1)
#9. Sort the first list from lowest to highest and print it.
h.sort()
print (h)