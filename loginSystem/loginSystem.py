import json

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
                newPassword = input("Create A Password: ")
                while True:
                    confirmPassword = input("Confirm Password: ")
                    if newPassword == confirmPassword:
                        newUser['password'] = confirmPassword
                        loginSystem.accounts.append(newUser)
                        with open (loginSystem.database, "w") as db:
                            json.dump(loginSystem.accounts, db, indent=4)

                        print("SUCCESS! " + newUser['username'] + " has been created.")
                        return 
                    else:
                        print("PASSWORDS DO NOT MATCH!")   

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

# print(loginSystem.accounts)
# loginSystem.userLogin()

# loginSystem.createAccount()


##Special Character Password##
# 1 capital letter
# 1 special char {!@#$%^&*<>?}
# 1 num
# len = 8
# specialChars = ["!", "@", "#", '$', "%", "^","&","*","<",">","?"]

# string = input(">>> ")
# check = False
# uppercaseCount = 0
# specialCharCount = 0
# numCount = 0
# for letter in string:
#     if len(string) >= 8:
#         if letter.isupper():
#             uppercaseCount += 1
#         if letter in specialChars:
#             specialCharCount += 1
#         if letter.isnumeric():
#             numCount += 1

# if (uppercaseCount >= 1) and (specialCharCount >= 1) and (numCount >=1):
#     check = True
# print(check)