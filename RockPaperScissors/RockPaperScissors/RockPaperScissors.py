import random

print("Hello, let's play!")
options = ["rock", "paper", "scissors", "lizard", "spock"]
rounds = input("How many rounds do you want to play? ")
try:
    numberOfRounds = int(rounds)
except ValueError:
    print("Can't you write a number???")
    quit()

relations = {
    "scissors": ["paper", "lizard"],
    "paper": ["rock", "spock"],
    "rock": ["lizard", "scissors"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

i = 0
while i < numberOfRounds:
    pcChoice = random.choice(options)
    userChoice = input("\nWhat's your choice? ")
    if userChoice.lower() not in options:
        print("You really don't know how to play this game...?!")
        continue
    print("PC chose " + pcChoice)

    if userChoice.lower() == pcChoice:
        print("Draw")
    elif userChoice.lower() in relations[pcChoice]:
        print("You lose")
    else:
        print("You win")
    i += 1

print("\nGood game!\n")
