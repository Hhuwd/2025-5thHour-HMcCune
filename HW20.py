#Name: Hogan McCune
#Class: 5th Hour
#Assignment: HW20

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Bam:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def georgia(self):
        self.cost *= 2
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
Bread = Bam(10, 5, 1)
NukaCola = Bam(8, 16, 5)
RAM = Bam(4, 199, 3)
#3. Print the stock of all three objects and the cost of the second store item.
print(Bread.stock)
print(NukaCola.stock)
print(RAM.stock)
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
print(NukaCola.cost)
NukaCola.georgia()
print(NukaCola.cost)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
RAM.stock *= (1/4)
RAM.stock = round(RAM.stock)
print(RAM.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del Bread
try:
    print(Bread.weight)
except:
    print("Error, Bread does not exist.")