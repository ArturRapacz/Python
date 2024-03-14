import logo
import random
import os
import time

def reset():
    global number
    global lowcounter
    global highcounter
    global mode
    global low
    global high
    number = random.randint(1,100)
    lowcounter = 0
    highcounter = 0
    mode = ""
    low = 1
    high = 100
    
play = True
reset()

print(logo.logo)
print("")

while play == True:
    time.sleep(2)
    print("I'm thinking of a number between 1 and 100.")
    if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == "easy":
        mode = "easy"
        guesses = 10
    else:
        mode = "hard"
        guesses = 5
        
    print(f"You have chosen {mode} mode. You have {guesses} guesses!")

    while guesses > 0:
        temp = int(input(f"Choose a number between {low} and {high} "))

        if temp == number:
            print(f"Congratulation! {temp} was a number I was thinking of! You won!")
            guesses = 0
            
        elif temp > number:
            guesses -= 1
            if guesses == 0:
                print("You lost!")
                continue
            print(f"Number I'm thinking of is lower. You have {guesses} more guesses.")
            if high > temp:
                high = temp
        else:
            guesses -= 1
            if guesses == 0:
                print("You lost!")
                continue
            print(f"Number I'm thinking of is higher. You have {guesses} more guesses.")
            if low < temp:
                low = temp
    
    if input("Do you want to play again? Y/N ").lower() == "y":
        reset()
        os.system('cls')
    else:
        print("Thank you for your time! It was incredible game!")
        play = False
        break
        