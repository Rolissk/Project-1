import random, sys, os, json
import time

from ieklusana import login, register, currentUser

from speles import secretNumber, rockPaperScissors, coinFlip, spinWheel, blackjack

from naudasShit import cashOut, shopMenu, inventory

def gameMenu():
    print('---------')
    print('Which game would you like to play? Every game costs 5 money to play!')
    print('---------')
    chosenGame = input("""
    If you'd like to play guess the secret number - (s) 
    If you'd like to play rock, paper, scissors - (r)
    If you'd like to play coin flip - (c)
    If you'd like to play spin the wheel - (w)
    If you'd like to play blackjack - (b)
    Chosen game:""").lower()
    if chosenGame =='s':
        secretNumber()
    if chosenGame =='r':
        rockPaperScissors()
    if chosenGame == 'c':
        coinFlip()
    if chosenGame == 'w':
        spinWheel()
    if chosenGame == 'b':
        blackjack()

def starts():
    while True:
        print('Welcome to the Arcade! \n Would you like to (l)og in, (r)egister or (q)uit?\n')
        ieeja=input('Enter your choice: ')
        if ieeja == 'l':
            login()
            print('\n----- Hello to the Arcade! -----\n')
            break
        elif ieeja == 'r':
            register()
            print('\n----- Hello to the Arcade! -----\n')
            break
        elif ieeja == 'q':
            sys.exit()
        else:
            print('Sorry, that is not a valid option.')
            continue

def moneyCheck():
    from ieklusana import userName
    print('---------')
    balCheck = userPath+"/userLog/" + userName+'.json'
    with open(balCheck) as data:
            money = json.load(data)
            data.close()
            print('You currently have '+ str(money['credits']) +' available.')
    print('---------')

with open('config.json') as f:
    config = json.load(f)
    f.close()

userPath =config['userPath']

starts()
#main loops
while True:
    izvele = input("""----------
    What would you like to do?\n
    You can check your balance by typing (b)
    You can pick a game to play by typing (g)
    You can cash out by typing (c)
    You can enter the shop by typing (s)
    You can check your inventory by typing (i)
    You can log out by typing (l)
    You can quit by typing (q)
    What will you do: """)
    if izvele == 'b':
        moneyCheck()
    elif izvele == 'g':
        gameMenu()
    elif izvele == 'c':
        cashOut()
    elif izvele == 's':
        shopMenu()
    elif izvele == 'i':
        inventory()
    elif izvele == 'l':
        print('Thank you for playing, goodbye!')
        starts()
    elif izvele == 'q':
        sys.exit()
    else:
        print('Sorry, that is not a valid option.')