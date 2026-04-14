#Name: Hogan McCune
#Class: 5th Hour
#Assignment: HW_R7


#1. Create a class containing a def function that inits self and the three attributes: name, grade, color.
class class1:
    def __init__(self, name, grade, color):
        self.name = name
        self.grade = grade
        self.color = color
    def add(self):
        if self.grade == 12:
            self.grade = "Graduated"
        else:
            self.grade = self.grade + 1
    def orion(self):
        self.color = input("Please Input/Change your favorite color!")
#2. Make a def function within the class that adds 1 to the grade attribute to any object called to it.
#If they are 12th grade, have the code change their grade to "graduated" instead.

#3. Make a def function within the class that offers the user to input/change their favorite color.
