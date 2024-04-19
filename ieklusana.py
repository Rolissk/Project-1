import os, sys, json

with open('config.json') as f:
    config = json.load(f)
    f.close()

userPath =config['userPath']
def currentUser():
    file_path = userPath
    file_name = "/currentuser.json"
    completePath = os.path.join(file_path, file_name)
    f= open(completePath, "w+")
    f.write('''
{
"userName":"'''+userName+'''"
}''')
    f.close()

def whosPlaying():
    whosPlayingPath = userPath + "/currentuser.json"
    with open(whosPlayingPath) as player:
        data = json.load(player)
        global userName
        userName = data['userName']
        return userName


def login():
    while True:
        global userName
        userName = input('Enter your username:\n')
        nameCheck = userPath + "/userLog/"+userName + ".json"
        if os.path.exists(nameCheck):
            print('Hello ' + userName + ', please enter your password:')
            break
        else: 
            print('Sorry, that username is not registered.')
    while True:
        userPass = input('Enter your password: ')
        passCheck = userPath + "/userLog/" + userName+'.json'
        with open(passCheck) as userData:
                data = json.load(userData)
                if data['password'] == userPass: 
                    currentUser()
                    break
                else:
                    print('Sorry, that password is incorrect.')
                    continue


def register():
    while True:
        newName = input('What should i call you? \n name: ')
        path = userPath + "/userLog/"+newName + ".json"
        if os.path.exists(path):
            print('Sorry, that username is already taken.')
            continue
        else:
            print('Hi,' + newName)
            newPass = input('Please enter your password (must be at least 8 characters in lenght):')
            if newPass == newName:
                print('Sorry, that password is the same as your name.')
            elif len(newPass) < 8:
                print('Password must be at least 8 characters in length.')
            elif ' ' in newPass:
                print('Password can\'t include blank spaces.')
            else:
                print('Thanks, '+ newName + ', you are now registered, you can log in now.\n')
                file_path = userPath + "/userLog"
                file_name = newName + ".json"
                completeName = os.path.join(file_path, file_name)
                f= open(completeName,"w+")
                newUser = ('''
{
"credits": 100,
"password": "'''+newPass+'''"
}''')
                f.write(str(newUser))
                f.close()

                inv_path = userPath + "/userLog"
                inv_name = newName + "Inv.json"
                completeInvName = os.path.join(inv_path, inv_name)
                f= open(completeInvName,"w+")
                inv={}
                f.write(str(inv))
                f.close()
                login()
                break

