import random
import os
import string
import time
scriptDir = os.path.dirname(__file__)



words = []
fh = open(scriptDir + "/words.txt", "r")
lines = fh.readlines()
for i in lines:
    words.append(i[:-1])


def getValidWord(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = getValidWord(words)
    wordLetters = set(word) #letters in word
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    lives = 6
    print("Welcome to Hangman Game!")
    time.sleep(1)
    while len(wordLetters) > 0 and lives > 0:
        #used letters
        print(f"You have {lives} lives left and you have used these letters: ", " ".join(usedLetters))

        wordList = [letter if letter in usedLetters else "-" for letter in word]
        print("Current word: ", " ".join(wordList))


        
        userLetter = input("Guess a letter: ").upper()
        if userLetter in alphabet and userLetter not in usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else: 
                lives -= 1
                print("Letter is not in word.")
                
                

        elif userLetter in usedLetters:
            print("You have already used this letter! Please try again.")
        else:
            print("Invalid character. Please try again.")
    if lives == 0:
        print(f"Sorry, you died. The word was {word}. Try your luck again!")
    else:
        print(f"You guessed the word {word}! CONGRATULATIONS!")


hangman()