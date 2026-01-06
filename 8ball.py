import random
eight_ball_responses = ("It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
                        "You may rely on it","As I see it, yes", "Most likely",
                        "Yes", "Signs point to yes","Don’t count on it", "My reply is no", "My sources say no", "Outlook not so good",
                        "Very doubtful")
year = random.randint(2025,2500)
y = input("Year or Question mode?")
while y == ("year") or y == "Year":
    input("What is your Question?")
    print(year)
    year = random.randint(2025, 2500)
while y != ("year") or y == "Year":
    x = input("What is your question?")
    print(random.choice(eight_ball_responses))