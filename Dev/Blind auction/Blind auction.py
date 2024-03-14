import os
import time
from logo import logo

maxbid=0
bidders = dict()
print("Blind Auction Simulator")
print(logo)
time.sleep(1)
print("Welcome in Blind Auction Simulator! I hope you will have fun!")
time.sleep(1)
while True:
    name = input("What is your name? ")
    time.sleep(1)
    bid = int(input("What is your maximum bid? "))
    time.sleep(1)
    bidders[name] = bid
    if bid > maxbid:
        maxbid = bid
    if input("Are there any other users who want to bid? Yes/No " ).lower() == "no":
        os.system('cls')
        break
    else:
        os.system('cls')
        time.sleep(1)


for i in bidders:
    if bidders[i] == maxbid:
        winner = i
for i in range(5):
    time.sleep(1)
    print("*"*(i+1))
time.sleep(1)
print(f"Ladies and Gentelmen!\nThe owner of the highest bid and also the winner is {winner}!\nThe highest bid value is ${maxbid}!")

