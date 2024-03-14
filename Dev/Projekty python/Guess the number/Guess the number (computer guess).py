import random
import time



def computerGuess(x):
    low = 1
    high = x
    feedback = ""
    print("Hi! My name is John and today I will be guessing what number are you thinking about!")
    time.sleep(1)
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low
        print(f"I guess... {guess}")
        time.sleep(1.5)
        feedback = input(f"Is guess {guess} too high (H), too low (L) or correct (C)?: ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        if feedback == "c":
            print(f"Yay! I've guessed correctly! {guess} is right number!")
        time.sleep(1)
computerGuess(10)