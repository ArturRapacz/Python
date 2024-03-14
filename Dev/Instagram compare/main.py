import logo
import data
import random
import os
import time

data = data.data
A = None
B = None
score = 0
play = True

def choicer():
    global A
    global B
    
    A = random.choice(data)
    B = random.choice(data)
    
    while A == B:
        B = random.choice(data)
    
def compare(A, B):
    global play
    global score
    if A["follower_count"] > B["follower_count"]:
        correctanswer = "A"
    else:
        correctanswer = "B"
    print(f"Compare A: {A["name"]}, {A["description"]}, from {A["country"]}")
    print(logo.vs)
    print(f"Compare B: {B["name"]}, {B["description"]}, from {B["country"]}")
    
    
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if correctanswer == answer:
        score += 1
        play = True
    else:
        play = False
        print(f"Sorry, that's wrong. Final score: {score}")

###### GAME ######
print(logo.logo)
print("In this game you have to choose which instagram profile has more followers\nHave fun!")
time.sleep(3)
os.system('cls')
while True:
    print(logo.logo)
    choicer()
    compare(A,B)

    while play == True:
        os.system('cls')
        print(logo.logo)
        print(f"You're right! Current score: {score}")
        choicer()
        compare(A,B)
    
    if input("Do you want to play again? Y/N: ").lower() == "y":
        os.system('cls')
        score = 0
        continue
    else:
        print("I hope you enjoyed the game!")
        break