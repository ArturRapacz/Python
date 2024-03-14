import time
import random

def play():
    print("Welcome to Rock, paper, scissors game! Have fun my friend!")
    time.sleep(1)
    user = ""
    again = "yes"
    userScore = 0
    computerScore = 0
    while again == "yes":
        
        user = input("Please write 'r' for rock, 's' for scissors' or 'p' for paper: ")
        computer = random.choice(["r", "p", "s"])

        if user == computer:
            print("It's a tie")
    
        elif isWin(user, computer):
            userScore += 1
            print(f"You won!")
        else:
            computerScore += 1 
            print(f"You lose :c")
        print(f"The score is \nYou: {userScore}   Computer: {computerScore}")
        again = input("Do you want to play again? yes/no: ")
        if again == "no" and userScore > computerScore:
            time.sleep(1)
            print(f"The score is {userScore}:{computerScore}, YOU WON VS COMPUTER")
        elif again == "no" and userScore < computerScore:
            time.sleep(1)
            print(f"The score is {userScore}:{computerScore}, YOU LOSE VS COMPUTER")
        elif again == "no" and userScore == computerScore:
            time.sleep(1)
            print(f"The score is {userScore}:{computerScore}, It's a tie! We need a rematch!")
    

def isWin(player, opponent):
    if player == "r" and opponent == "s" or player == "s" and opponent == "p" or player == "p" and opponent == "rock":
        return True
    
play()