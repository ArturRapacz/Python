import random
import time


def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0 
    while guess != randomNumber:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < randomNumber:
            print("Sorry, guess again. Too low.")
            time.sleep(1)
        elif guess > randomNumber:
            print("Sorry, guess again. Too high")
            time.sleep(1)
    time.sleep(1)
    print(f"Congrats! you have guessed the number {randomNumber} correctly!")

guess(10)