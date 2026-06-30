import random

print("Welcome To My Quiz Game")

Playing = input("Do yo want to play")

if Playing != "yes":
    quit()

print("Okay Lets Play The Game")
score = 0

Answer = input("Which is the capital of france?")
if Answer.lower() == "paris":
    print("correct")
    score +=1
else:
    print("incorrect")

Answer = input("Which is the capital of Pakistan?")
if Answer.lower() == "islamabad":
    print("correct")
    score +=1
else:
    print("incorrect")

Answer = input("Which is the capital of India?")
if Answer.lower() == "new delhi":
    print("correct")
    score +=1
else:
    print("incorrect")

Answer = input("Which is the capital of Australia?")
if Answer.lower() == "canberra":
    print("correct")
    score +=1
else:
    print("incorrect")

print("You got"+str(score)+ "questions correct")
print("You got"+str((score/4)*100) + "%")
