import random, sys, time
from naudasShit import addMoney, takeMoney
def secretNumber():
    print('Hello to he secret number game!\nYou will have 6 attempts to guess the number!')
    while True:
        takeMoney(5)
        secretNumb = random.randint(1,30)
        print('Im thinking of  anumber between 1 and 30')

        for guessesTaken in range(1,6):
            print('Take a guess')
            guess=int(input())

            if guess<secretNumb:
                print('Guess is too low')
            elif guess>secretNumb:
                print('Guess is too high')
            else:
                break

        if secretNumb == guess:
            print('Congrats, you guessed it in ' +str(guessesTaken) +' guesses and you\'ve earned 10 points!')
            addMoney(10)
        else:
            print('The number i was thinking of was ' +str(secretNumb) +'!')
        snizvele = input('If you\'d like to play again, type (a) or press enter to quit!')
        if snizvele == 'a':
            continue
        elif snizvele == '':
            break

def rockPaperScissors():
    print('ROCK, PAPER, SCISSORS')
    while True:
        takeMoney(5)
        while True:
            print('Your turn: (r)ock (p)aper (s)cissors')
            plMove = input()
            if plMove == 'r' or plMove =='p' or plMove =='s':
                break
            print('type one of r, p, s.')
        
        if plMove == 'r':
            print('Rock vs')
        elif plMove == 'p':
            print('Paper vs')
        elif plMove == 's':
            print('Scissors vs')

        randomNum = random.randint(1,3)
        if randomNum == 1:
            comMove = 'r'
            print('Rock')
        elif randomNum == 2:
            comMove = 'p'
            print('Paper')
        elif randomNum == 3:
            comMove = 's'
            print('Scissors')
        
        if plMove == comMove:
            print('Its a Tie, you get your money back!')
            addMoney(5)
        elif plMove == 'r' and comMove == 's':
            print('You win!')
            addMoney(10)
        elif plMove == 'p' and comMove == 'r':
            print('You win!')
            addMoney(10)
        elif plMove == 's' and comMove == 'p':
            print('You win!')
            addMoney(10)
        elif plMove == 'r' and comMove == 'p':
            print('You lose')
        elif plMove == 'p' and comMove == 's':
            print('You lose')
        elif plMove == 's' and comMove == 'r':
            print('You lose')
        rpsizvele = input('If you want to play again, type (a) or press enter to quit')
        if rpsizvele == 'a':
            continue
        elif rpsizvele == '':
            break
    

def coinFlip():
    while True:
        takeMoney(5)
        coinPick = input('Pick your side of the coin: (h)eads or (t)ails!')
        if coinPick == 'h':
            print('You call heads!')
        elif coinPick == 't':
            print('You call tails!')
        coinRng = random.randint(0,1) 
        if coinRng == 0:
            coinRng = 'h'
            print('Coin has landed on the head!')
            if coinPick == coinRng:
                addMoney(10)
                print('You win!')
            else:
                print('You lose!')
        if coinRng == 1:
            coinRng = 't'
            print('Coin has landed on the tails!')
            if coinPick == coinRng:
                addMoney(10)
                print('You win!')
            else:
                print('You lose!')
        cfizvele = input('If you want to play again, type (a) or press enter to quit!')
        if cfizvele == 'a':
            continue
        if cfizvele == '':
            break

def spinWheel():
    print("""Welcome to spin the wheel!
    Get 2 of the same number and win, get 3 and get the jackpot!""")
    while True:
        print('If you want to play, type (spin), press enter to quit')
        atbilde = input()
        if atbilde == 'spin':
            takeMoney(5)
            print('Spinning the wheel!\n')
            pirmais = random.randint(1,5)
            print('1st number is ' + str(pirmais))
            otrais = random.randint(1,5)
            print('2nd number is ' + str(otrais))
            tresais = random.randint(1,5)
            print('3rd number is ' + str(tresais))
        elif atbilde == '':
            break
        if pirmais == otrais and pirmais == tresais and otrais == tresais:
            print('JACKPOT!')
            addMoney(20)
        elif pirmais == otrais or pirmais == tresais or otrais == tresais:
            print('You won a small prize!')
            addMoney(10)
        else:
            print('You lost!')

def blackjack():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_value = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
                '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A11':11, 'A1':1}
    global dlHandVal
    global plHandVal
    plHandVal = 0
    dlHandVal = 0

    def firstPlCard():
        global plHandVal
        pirmKart = random.choice(deck)
        print('Your 1st card is: ' +pirmKart + ' !')
        if pirmKart == 'A':
            plHandVal = 11
        elif pirmKart in card_value:
            plHandVal = card_value[pirmKart]
        otrKart = random.choice(deck)
        print('Your 2nd card is: ' +otrKart + ' !')
        if otrKart == 'A':
            plHandVal = 11
        elif otrKart in card_value:
            plHandVal += card_value[otrKart]
        time.sleep(0.3)
        print('Value of your hand is: ' +str(plHandVal) + ' !')

    def firstDlCard():
        global dlHandVal
        pirmKartDl = random.choice(deck)
        print('Dealers card is: ' +pirmKartDl + ' !')
        if pirmKartDl == 'A':
            dlHandVal = 11
        elif pirmKartDl in card_value:
            dlHandVal = card_value[pirmKartDl]
        print('Value dealers hand is: ' +str(dlHandVal) + ' !')

    def PlChoice():
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        while True:
            global plHandVal
            global izvele
            izvele = input('Would you like to (h)it or (s)tand?\nChoice: ').lower()
            if izvele == 'h':
                tresKartPl=random.choice(deck)
                print('You hit: '+ tresKartPl +' !')
                if tresKartPl == 'A':
                    if plHandVal >= 11:
                        ace = 1
                    else:
                        ace = 11
                    plHandVal = plHandVal + ace
                    time.sleep(0.3)
                    print('Value of your hand is: '+ str(plHandVal)+' !\n ')
                else:
                    plHandVal = plHandVal + card_value[tresKartPl]
                    time.sleep(0.3)
                    print('Value of your hand is: '+ str(plHandVal)+' !\n ')
                if plHandVal == 21:
                    print('You win')
                    break
                elif plHandVal > 21:
                    print('You lose')
                    break
            elif izvele =='s':
                print('Standing at value: '+ str(plHandVal) +' !\n ')
                time.sleep(0.3)
                secondDlCard()
                break
            else:
                print('Please type h or s')
                continue

    def secondDlCard():
        global dlHandVal
        otrKartDl = random.choice(deck)
        print('Dealers card is: ' +otrKartDl + ' !')
        if otrKartDl == 'A':
            if dlHandVal > 11:
                ace = 1
            else:
                ace = 11
            dlHandVal = dlHandVal + ace
            time.sleep(0.3)
            print('Value dealers hand is: ' +str(dlHandVal) + ' !\n ')
        else:
            dlHandVal = dlHandVal + card_value[otrKartDl]
            time.sleep(0.3)
            print('Value dealers hand is: ' +str(dlHandVal) + ' !\n ')
            
    print("""Welcome to Blackjack!
    Goal of the game is to hit 21 or have a higher number than the dealer!""") 
    while True:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        speletVaiNe= input('Would you like to play?\n(Y)es or (N)o\n:').lower()
        if speletVaiNe == 'n':
            break
        elif speletVaiNe == 'y':
            while True:
                takeMoney(5)
                print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
                firstDlCard()
                time.sleep(0.3)
                firstPlCard()
                if plHandVal == 21:
                    print('You Win')
                    addMoney(10)
                    break
                else:
                    PlChoice()
                if plHandVal >=21:
                    break
                while True:
                    if dlHandVal < 17:
                        secondDlCard()
                        continue
                    if dlHandVal >= 17:
                        break
                if plHandVal > dlHandVal:
                    print('You Win')
                    addMoney(10)
                    break
                elif dlHandVal > 21:
                    print('You win')
                    addMoney(10)
                    break
                elif plHandVal < dlHandVal:
                    print('You lose')
                    break
                else:
                    print('It is a tie')
                    addMoney(5)
                    break
            