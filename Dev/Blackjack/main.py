from logo import *
import random
import os
import time

print(logo)
print("Welcome in Blackjack game! Have fun!")

cards = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "queen", "king", "jack"]
specialcards = ["queen", "king", "jack"]
computer = [random.choice(cards), random.choice(cards)]
player = [random.choice(cards), random.choice(cards)]
computerscore = 0
playerscore = 0

for i in computer:
    if i == "ace":
        computerscore += 11
    elif i in specialcards:
        computerscore += 10
    else:
        computerscore += i
    
for i in player:
    if i == "ace":
        playerscore += 11
    elif i in specialcards:
        playerscore += 10
    else:
        playerscore += i
    
print(f"Your cards: {", ".join(str(i) for i in player)}")        
while True:
    if input("Do you want to grab another card? Y/N ").lower() == "y":
        player.append(random.choice(cards))
        print(f"Your cards: {", ".join(str(i) for i in player)}")
        if player[-1] == "ace":
            if input("Do you want to use ace as an 1 or 11? ") == "1":
                playerscore += 1
            else:
                playerscore += 11   
        elif player[-1] in specialcards:
            playerscore += 10
        else:
            playerscore += player[-1]
        if playerscore == 21:
            print("You have a blackjack! You won!")
            if input("Do you want play again? Y/N ").lower() == "y":
                os.system('cls')
                computer = [random.choice(cards), random.choice(cards)]
                player = [random.choice(cards), random.choice(cards)]
                computerscore = 0
                playerscore = 0
                for i in computer:
                    if i == "ace":
                        computerscore += 11
                    elif i in specialcards:
                        computerscore += 10
                    else:
                        computerscore += i
                    

                for i in player:
                    if i == "ace":
                        playerscore += 11
                    elif i in specialcards:
                        playerscore += 10
                    else:
                        playerscore += i
                print(f"Your cards: {", ".join(str(i) for i in player)}") 
                continue
            else:
                break
        if playerscore > 21:
            print("You lose!")
            if input("Do you want play again? Y/N ").lower() == "y":
                os.system('cls')
                computer = [random.choice(cards), random.choice(cards)]
                player = [random.choice(cards), random.choice(cards)]
                computerscore = 0
                playerscore = 0
                for i in computer:
                    if i == "ace":
                        computerscore += 11
                    elif i in specialcards:
                        computerscore += 10
                    else:
                        computerscore += i
                    
                for i in player:
                    if i == "ace":
                        playerscore += 11
                    elif i in specialcards:
                        playerscore += 10
                    else:
                        playerscore += i
                print(f"Your cards: {", ".join(str(i) for i in player)}") 
                continue
            else:
                break
        else:
            continue
    else:
        while True:
            computer.append(random.choice(cards))
            print(f"Computer cards: {", ".join(str(i) for i in computer)}")
            if computer[-1] == "ace":
                if computerscore + 11 > 21:
                    computerscore += 1
                else:
                    computerscore += 11   
            elif computer[-1] in specialcards:
                computerscore += 10
            else:
                computerscore += computer[-1]
            if computerscore == 21:
                print("Computer has a blackjack! You lose!")
                break
            elif computerscore > 21:
                print("Computer score is over 21: You win!")
                break
            elif computerscore < 17:
                time.sleep(2)
                continue
            else:
                if computerscore > playerscore:
                    print("Computer score is higher! You lose!")
                elif computerscore < playerscore:
                    print("You score is higher! You win!")
                else:
                    print("IT'S A DRAW!!!")
                break
        if input("Do you want to play again? Y/N ").lower() == "n":
            break
        else:
            os.system('cls')
            computer = [random.choice(cards), random.choice(cards)]
            player = [random.choice(cards), random.choice(cards)]
            print(f"Your cards: {", ".join(str(i) for i in player)}")
            computerscore = 0
            playerscore = 0
            for i in computer:
                if i == "ace":
                    computerscore += 11
                elif i in specialcards:
                    computerscore += 10
                else:
                    computerscore += i

            for i in player:
                if i == "ace":
                    playerscore += 11
                elif i in specialcards:
                    playerscore += 10
                else:
                    playerscore += i