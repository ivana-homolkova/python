import random

print("Welcome to the game! How many of you are there?")
numberOfContestants = input()
try:
    numberOfContestants2 = int(numberOfContestants)
except ValueError:
    quit()

listOfNames = []
c = 0
while c < numberOfContestants2:
    contestantName = input("State your name. ")
    listOfNames.append(contestantName)
    c += 1
else:
    print("Welcome " + str(listOfNames) + " to the game.")

questions = {
    "animals" : {
        "Is spider an insect?" : "no",
        "Does platypus give birth?" : "no"
        },
    "history" : {
        "Could Cleopatra watch pyramids being build?" : "no",
        "Did Columbus discover America?" : "no"
        },
    "human body" : {
        "Is femur the strongest bone?" : "yes",
        "is there over 100 bones in a human body?" : "yes"
        }
    }

def pickQuestion(i = 0):
    print(str(listOfNames[i]) + ", do you want question about history, animals or human body?")
    topic = input().lower()

    if topic in questions:
        questionTopic = questions[topic]
        questionChoice = random.choice(list(questionTopic.keys()))
        print(questionChoice)

        answer(questionChoice, questionTopic)
        questions[topic].pop(questionChoice)

    else:
        print("You can't write!")

def answer(question, topic):
    answerChoice = input("What is your answer? ").lower()
    
    if answerChoice == topic[question]:
        print("Correct!")
    else:
        print("Incorrect! The right answer was " + topic[question])

for i in range(numberOfContestants2):
    pickQuestion(i)