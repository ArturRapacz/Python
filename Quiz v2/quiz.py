import time

print("Welcome to my computer quiz! I hope you will have fun!")

playQuestion = input("Do you want to play? \nAnswer yes or no ")

if playQuestion != "yes":
    time.sleep(3)
    "That's sad! :C"
    quit()

answer = input("What does CPU stand for")