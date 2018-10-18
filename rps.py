import random
import string
import time
import sys
import pymongo
from pymongo import MongoClient

options = ['Rock', 'Paper', 'Scissors']
paper = 'Paper'
rock = 'Rock'
scissors = 'Scissors'

while True:
    asdf = random.choice(options)
    resultid = "".join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    client = MongoClient('YOUR_MONGO_ADDRESS')
    db = client.rpsvalidator
    collection = db.results
    res = collection.find_one({"resultid": resultid})
    if res == None:
        print('Result ID Generated')
        break
    else:
        print('Found RID in database, retrying')
        break
while True:
    player1 = input('Rock, Paper or Scissors? (CaSe SeNsItIvE!): ')
    if player1 in to_guess:
        print('Oops! You and the computer picked the same! Restart the game. \n Closing in 3 seconds...')
        time.sleep(3)
        sys.exit()
    elif player1 in "RockPaperScissors":
        if paper in player1:
            if scissors in to_guess:
                print(
                    '*chop chop* The computer\'s scissors destroy your paper. You lost.\n Thanks for playing! Closing in 3 seconds.')
                result = {"computer": "scissors", "player": "paper", "resultid": resultid}
                collection.insert_one(result)
                print(f'Your result ID is: {resultid}')
                time.sleep(3)
                sys.exit()
            if rock in to_guess:
                print('You won! *Paper crumples on computer\'s rock*\n Thanks for playing! Closing in 3 seconds...')
                result = {"computer": "rock", "player": "paper", "resultid": resultid}
                collection.insert_one(result)
                print(f'Your result ID is: {resultid}')
                time.sleep(3)
                sys.exit()
        if rock in player1:
            if paper in to_guess:
                print('*paper crumples on your rock* You lost. Sorry!\n Thanks for playing! Closing in 3 seconds...')
                result = {"computer": "paper", "player": "rock", "resultid": resultid}
                collection.insert_one(result)
                print(f'Your result ID is: {resultid}')
                time.sleep(3)
                sys.exit()
            if scissors in to_guess:
                print(
                    '*clang* Your rock destroys the computer\'s scissors. You win!\n Thanks for playing! Closing in 3 seconds...')
                result = {"computer": "scissors", "player": "rock", "resultid": resultid}
                collection.insert_one(result)
                print(f'Your result ID is: {resultid}')
                time.sleep(3)
                sys.exit()
        if scissors in player1:
            if paper in to_guess:
                print(
                    '*chop, chop* You cut up the computer\'s paper. You win!\n Thanks for playing! Closing in 3 seocnds...')
                result = {"computer": "paper", "player": "scissors", "resultid": resultid}
                collection.insert_one(result)
                print(f'Your result ID is: {resultid}')
                time.sleep(3)
                sys.exit()
            if rock in to_guess:
                print(
                    '*clanging* The computer\'s rock bends your scissors to hell and back. You lose.\n Thanks for playing! Closing in 3 seconds...')
                result = {"computer": "rock", "player": "scissors", "resultid": resultid}
                collection.insert_one(result)
                print(f'Your result ID is: {resultid}')
                time.sleep(4)
                sys.exit()
