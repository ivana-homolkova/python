from Class1 import Question
from Questions import questions
import random

def play():
    random.shuffle(questions)

    guess = ""
    score = 0

    input("You're going to get 5 questions. Ready? ")

    for i in range(min(len(questions), 5)):
        question = questions[i]
        print(question.ques)
        guess1 = input("What is your guess? ")
        guess = guess1.lower()

        while guess not in ["a", "b", "c", "d"]:
            print("You need to choose from a, b, c or d!")
            guess1 = input("What is your guess? ")
            guess = guess1.lower()

        if guess == question.asw:
            print("Correct")
            score += 1
        else:
            print("Incorrect")

    print("Your score is " + str(score) + " out of " + str(min(len(questions), 5)))
    if score <= 2:
        print("That was a weak attemt...")
    elif score <= 4:
        print("Could be better.")
    else:
        print("Nice!")

while True:
    play()
    again = input("Do you want to play again? 'yes' 'no' ")
    if again != "yes":
        break