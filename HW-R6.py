#Name: Hogan McCune
#Class: 5th Hour
#Assignment: HW-R6


#1. Create a def function that prints out "Hello World!". Call the function.
def test():
    print("Hello World!")

test()
#2. Create a def function that prints your name. Call the function with the name as the argument.
def name(studentname):
    print(studentname)

name("Hogan")
#3. Create a def function that calculates the average of a list. Call the function with the list as the argument.
def average_list(*num_list):
    avg = sum(num_list)/len(num_list)
    print(avg)

average_list(21,45,3,999,356,1)
#4. Call the function from #3 but with a new list of different numbers.
average_list(2351,44535,35,12,416,3)
#5. Create a def function that takes two numbers as arguments, x and y. Inside the function, create a for loop
#with a range of 10. Inside the loop, make z equal the sum of x and y, make x equal y, then y equal z. Then Print X.
def fib(x, y):
    for a in range(10):
        z = x + y
        x = y
        y = z
        print(x)
#6. Call the function from #5 with the arguments for x and y being 0 and 1.
fib(0,1)