import json

class loginSystem:
    database = "./data.json"
    with open (database, "r") as db:
        accounts = json.load(db)

    testDict = {}
    for account in accounts:
        username = account['username']
        testDict[username] = account['password']

    # def createAccount():
    #     item['username'] = input("New Username: ")
    #     item['password'] = input("New Password: ")

    #     loginSystem.accounts.append(item)

    #     with open (loginSystem.database, "w") as db:
    #         json.dump(loginSystem.accounts, db, indent=4)

    def userLogin():
        while True:
            username = input("Username: ")
            if username in loginSystem.testDict:
                while True:
                    password = input('Password: ')
                    if password == loginSystem.testDict[username]:
                        print("SUCCESS")
                        break
                    else:
                        print("WRONG PASSWORD!")
                break
            else:
                print("USER NOT FOUND")

    def createAccount():
        newUser = {}
        while True:
            newUser['username'] = input("Create username: ")
            if newUser['username'] in loginSystem.testDict:
                print("Username TAKEN! Try again...")
            else:
                newUser['password'] = input("Create a password: ")
                loginSystem.accounts.append(newUser)

                with open (loginSystem.database, "w") as db:
                    json.dump(loginSystem.accounts, db, indent=4)

                print("SUCCESS! " + newUser['username'] + " has been created.")
                break

    def main():
        prompt = input("Login or Create Account? ")

        if prompt == "Login" or prompt == "login":
            loginSystem.userLogin()
        elif prompt == "Create Account" or prompt == "create account":
            loginSystem.newUser()
        else:
            loginSystem.main()

# loginSystem.main()

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
