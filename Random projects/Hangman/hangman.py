import random

word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)
wordshow = "_"*len(word)
letterlist = []
lives = 3

print(f"Welcome in Hangman Game! Good Luck!\nYour word has {len(word)} letters and you have {lives} lives!")
      
while True:
    guess = input("Guess a letter: ")
    if guess.lower() in letterlist:
        print(f"Letter {guess} was already used. Try again.")
        continue
    else:
        letterlist.append(guess.lower())
    if guess in word:
        wordshow = list(wordshow)
        for i in range(len(word)):
            if word[i] == guess:
                wordshow[i] = guess
        wordshow = "".join(wordshow)
        used = ", ".join(letterlist)
        if wordshow == word:
            print(f"Congratulations! You won!\nThe word was '{word}'")
            question = input("Do you want to play again? Y/N ")
            if question.upper() == "Y":
                word = random.choice(word_list)
                wordshow = "_"*len(word)
                letterlist = []
            else:
                print("Thank you for playing a game!")
                break
                
        else:
            print(f'Congratulations! Letter {guess} is in your word! There is a list of used letters: {used}')
    else:
        if lives == 1:
            print("You lost!")
            question = input("Do you want to play again? Y/N ")
            if question.upper() == "Y":
                word = random.choice(word_list)
                wordshow = "_"*len(word)
                letterlist = []
            else:
                print("Thank you for playing a game!")
                break
        else:
            lives -= 1
            print(f"This time you failed. Letter {guess} is not in your word. You still have {lives} lives!")
          
    
    if wordshow == word:
        print(f"Congratulations! You won!\nThe word was '{word}'")
        break
    else: print(wordshow)
    

    
    
    
