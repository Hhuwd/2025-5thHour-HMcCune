#Name: Hogan McCune
#Class: 5th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
w = int(input("Input number of players:"))
o = (0)
if w < 3:
    print("Too little players!")
    quit()
for b in range(1,w+1):
    h = int(input("Please rate the model from 1-5:"))
    while h > 5 or h < 1:
       print("ERROR")
       h = int(input("Please rate the model from 1-5:"))
    else:
        o += h
print(o / w)