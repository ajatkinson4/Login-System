#Special Character Password##
# 1 capital letter
# 1 special char {!@#$%^&*<>?}
# 1 num
# len = 8

def checkSpecialPassword(password):
    specialChars = ["!", "@", "#", '$', "%", "^","&","*","<",">","?"]
    # string = input(">>> ")
    uppercaseCount = 0
    specialCharCount = 0
    numCount = 0
    for letter in password:
        if len(password) >= 8:
            if letter.isupper():
                uppercaseCount += 1
            if letter in specialChars:
                specialCharCount += 1
            if letter.isnumeric():
                numCount += 1

    if (uppercaseCount >= 1) and (specialCharCount >= 1) and (numCount >=1):
        return True
    else:
        print("PASSWORD MUST HAVE: \n * 8 Letters \n * 1 Capital Letter \n * 1 Special Char {!@#$%^&*<>?} \n * 1 Number")
        return False