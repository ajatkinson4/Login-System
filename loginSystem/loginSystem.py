import json
from specialPassword import *

class loginSystem:
    database = "./data.json"
    with open (database, "r") as db:
        accounts = json.load(db)
    tempDatabase = {}

    def updateTempDatabase():
        loginSystem.database = "./data.json"
        with open (loginSystem.database, "r") as db:
            loginSystem.accounts = json.load(db)
        loginSystem.tempDatabase = {}


        for account in loginSystem.accounts:
            username = account['username']
            loginSystem.tempDatabase[username] = account['password']

    def userLogin():
        loginSystem.updateTempDatabase()
        while True:
            username = input("Username: ")
            if username in loginSystem.tempDatabase:
                while True:
                    password = input('Password: ')
                    if password == loginSystem.tempDatabase[username]:
                        print("SUCCESS")
                        # break
                        return
                    else:
                        print("INCORRECT PASSWORD!")
            else:
                print("USER NOT FOUND")

    def createAccount():
        loginSystem.updateTempDatabase()
        newUser = {}
        while True:
            newUser['username'] = input("Create Username: ")
            if newUser['username'] in loginSystem.tempDatabase:
                print("Username TAKEN! Try Again...")
            else:
                loginSystem.createPassword(newUser)
                return
                

    def createPassword(newUser):
        while True:
            newPassword = input("Create A Password: ")

            if checkSpecialPassword(newPassword):
                confirmPassword = input("Confirm Password: ")
                if newPassword == confirmPassword:
                    newUser['password'] = confirmPassword
                    loginSystem.accounts.append(newUser)
                    with open (loginSystem.database, "w") as db:
                        json.dump(loginSystem.accounts, db, indent=4)

                    print(f"SUCCESS! {newUser['username']} has been created.")
                    return
                else:
                    print("PASSWORDS DO NOT MATCH!")
            else:
                continue

    def deleteAccount():
        loginSystem.updateTempDatabase()
        newData = []
        while True:
            username = input("Username: ")
            if username in loginSystem.tempDatabase:
                while True:
                    password = input("Password: ")
                    if password == loginSystem.tempDatabase[username]:
                        confirmPassword = input("Confirm Password to DELETE Account: ")
                        if password == confirmPassword:
                            for account in loginSystem.accounts:
                                if username in account['username'] and password in account['password']:
                                    pass
                                else:
                                    newData.append(account)
                            with open(loginSystem.database, "w") as db:
                                json.dump(newData, db, indent=4)
                            print(username + " has been DELETED.")
                            return
                        else:
                            print("PASSWORDS DO NOT MATCH!!")
                    else:
                        print("INCORRECT PASSOWRD!")
            else:
                print("Username DOES NOT Exists!")
            
    def main():
        prompt = input("------------------------\nLogin | Create Account | Delete Account\n>>> ")

        if prompt == "Login" or prompt == "login":
            loginSystem.userLogin()
            loginSystem.main()
        elif prompt == "Create Account" or prompt == "create account" or prompt == "create":
            loginSystem.createAccount()
            loginSystem.main()
        elif prompt == "Delete Account" or prompt == "delete account" or prompt == "delete":
            loginSystem.deleteAccount()
            loginSystem.main()
        elif prompt == "Exit" or prompt == "exit" or prompt == "X" or prompt == "x":
            return
        else:
            loginSystem.main()

loginSystem.main()

# password = input(">>> ")
# checkSpecialPassword(password)