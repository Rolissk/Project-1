import random, sys, os, json
from ieklusana import currentUser, whosPlaying

with open('config.json') as f:
    config = json.load(f)
    f.close()

userPath =config['userPath']
def cashOut():
    print('---------')
    while True:
        from ieklusana import userName
        balCheck = userPath + "/userLog/" + userName+'.json'
        with open(balCheck) as data:
            money = json.load(data)
            data.close()
            print('You currently have '+ str(money['credits']) +' available.')
        moneyOut = input('How much would you like to cash out? (write a decimal number)')
        if moneyOut.isalpha():
            print('Sorry, that is not a number.')
        elif moneyOut > str(money['credits']):
            print('Sorry, you do not have that much money.')
            break
        elif moneyOut <= str(money['credits']):
            with open(balCheck) as money:
                moneyData = json.load(money)
                money.close()
                moneyData['credits'] -= int(moneyOut)
                pathOut = userPath + "/userLog/" +str(userName)+".json"
                with open(pathOut, 'w') as outfile:
                    json.dump(moneyData, outfile,indent=4)
                    break

def shopMenu():
    print('---------')
    print('Welcome to the prize shop!\n Here you can exchange your money for a prize!')
    shopIzvele = input('If you want to see prizes - (p), or press enter to quit!')
    if shopIzvele == 'p':
        while True:
            from ieklusana import userName
            shop = userPath + "/userLog/shopItems.json"
            with open(shop) as data:
                shopItems = json.load(data)
                data.close()
            for key, value in shopItems.items():
                print(key +' - '+str(value))
            shopIzvele = input('Would you like to purchase any of the items? (y) or (n)').lower()
            if shopIzvele == 'n':
                break
            elif shopIzvele == 'y':
                global koPirkt
                koPirkt = input('Which item would you like to purchase? (write the name of the item)\n')
                if koPirkt == 'bear':
                    stockCheck(koPirkt)
                    if stock == 'out':
                        print('Sorry, we are out of stock.')
                        break
                    else:
                        print('Bear costs 20 coins')
                    moneyCheck(20)
                    if noBal == 'out':
                        print("Sorry, you dont have enough money to purchase")
                        break
                    pirktIzvele = input('Would you like to buy it? (y) or (n)').lower()
                    if pirktIzvele == 'y':
                        takeMoney(20)
                        buyingPick()
                    else:
                        break
                elif koPirkt == 'bow and arrow':
                    stockCheck(koPirkt)
                    if stock == 'out':
                        print('Sorry, we are out of stock.')
                        break
                    else:
                        print('Bow and arrow costs 30 coins')
                    moneyCheck(30)
                    if noBal == 'out':
                        print("Sorry, you dont have enough money to purchase")
                        break
                    pirktIzvele = input('Would you like to buy it? (y) or (n)').lower()
                    if pirktIzvele == 'y':
                        takeMoney(30)
                        buyingPick()
                    else:
                        break
                elif koPirkt == 'toy car':
                    stockCheck(koPirkt)
                    if stock == 'out':
                        print('Sorry, we are out of stock.')
                        break
                    else:
                        print('Toy car costs 50 coins')
                    moneyCheck(50)
                    if noBal == 'out':
                        print("Sorry, you dont have enough money to purchase")
                        break
                    pirktIzvele = input('Would you like to buy it? (y) or (n)').lower()
                    if pirktIzvele == 'y':
                        takeMoney(50)
                        buyingPick()
                    else:
                        break

def moneyCheck(ammount):
    from ieklusana import userName
    balCheck = userPath + "/userLog/" + userName+'.json'
    with open(balCheck) as data:
        money = json.load(data)
        data.close()
        if money['credits'] < int(ammount):
            global noBal
            noBal = 'out'
        else:
            noBal = 'in'
def stockCheck(item):
    shop = userPath + "/userLog/shopItems.json"
    with open(shop) as data:
        shopItems = json.load(data)
        data.close()
        if item in shopItems:
            if shopItems[item] == 0:
                global stock
                stock = 'out'
            else:
                stock = 'in'

def buyingPick():
    from ieklusana import userName
    global koPirkt
    path = userPath + "/userLog/" +str(userName)+"Inv.json"
    with open(path) as inventoryFile:
        inventAdd = json.load(inventoryFile)
        if koPirkt not in inventAdd:
            count = 1
            inventAdd[koPirkt] = count
        else:
            count = 1
            inventAdd[koPirkt] += count
        with open(path, 'w') as outfile:
            json.dump(inventAdd, outfile,indent=4)
            shop = userPath + "/userLog/shopItems.json"
            with open(shop) as data:
                shopItems = json.load(data)
                data.close()
                shopItems[koPirkt]-=1
            with open(shop,'w') as newShop:
                json.dump(shopItems,newShop,indent =4)
def inventory():
    print('---------\nInventory:')
    from ieklusana import userName
    invPath = userPath + "/userLog/"+str(userName)+"Inv.json"
    with open(invPath) as inv:
                invItems = json.load(inv)
                inv.close()
                for key, value in invItems.items():
                    print( key +' - '+str(value))
    print('---------')

def addMoney(ammount):
    from ieklusana import userName
    path = userPath + "/userLog/" +str(userName)+".json"
    with open(path) as money:
        moneyData = json.load(money)
        money.close()
        moneyData['credits'] += int(ammount)
        pathOut = userPath + "/userLog/" +str(userName)+".json"
        with open(pathOut, 'w') as outfile:
            json.dump(moneyData, outfile,indent=4, )
        
    
def takeMoney(ammount):
    from ieklusana import userName
    path = userPath + "/userLog/" +str(userName)+".json"
    with open(path) as money:
        moneyData = json.load(money)
        money.close()
        moneyData['credits'] -= int(ammount)
        pathOut = userPath + "/userLog/" +str(userName)+".json"
        with open(pathOut, 'w') as outfile:
            json.dump(moneyData, outfile,indent=4, )
