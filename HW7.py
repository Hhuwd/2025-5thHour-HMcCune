#Name: Hogan McCune
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print ("Hello World!")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
diktonary = {
    "Number of Wars": 3,
    "Nukes Used": 12,
    "Dates of Wars": [1914, 1939, 2034]
}
#3. Print the keys of the dictionary from #2.
print (diktonary)
#4. Print the values of the dictionary from #2
print(diktonary.values())
#5. Print one of the three numbers from the list by itself
print(diktonary["Dates of Wars"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
diktonary.update( {"Antimatter Weapon used": 1})
#7. Print the entire dictionary from #2 with the updated key and value.
print (diktonary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
Roster = {
    "Student1": {
        "Name": "Waylon",
        "Army Deployed In": "US Navy",
        "Status": "Dead"
    },
   "Student2": {
        "Name": "Diana",
        "Army Deployed In": "US Army",
        "Status": "Dead"
    },
   "Student3": {
        "Name": "Mardy",
        "Army Deployed In": "Russian Hyperstate Spy Services",
        "Status": "Alive"
    }
}
#9. Print the names of all three classmates on the same line.
print (Roster["Student3"]["Name"],Roster["Student2"]["Name"], Roster["Student1"]["Name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
Roster.pop("Student3")
print (Roster)