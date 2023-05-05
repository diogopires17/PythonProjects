import  os
import hashlib
clear = lambda: os.system('cls')

def main():
    clear()
    print("Menu")
    print("---------------------------")
    print("\n")
    print("1- Registar")
    print("2- Login")

    while(True):
        choice = input("Introduce a number:")
        if choice in ['1', '2']:
            break
    if choice == '1':
        Register()
    else:
        login()



def Register():
    clear()
    print("-----------------------------")
    print("Register mode:")
    print("-----------------------------")
    print("\n")
    while(True):
        user = input("User name:").title
        if user != '':
            break
    user = sanitize(user)
    
    while(True):
        password = input("Password")
        if password != '':
            break
    while(True):
        password_match = input("Confirm Password")
        if password_match == password:
            break
        else:
            print("Passwords are diferent!")
            print("\n")
        if userAlreadyExists(user, password):
            while(True):
                error = input("User already exists! Do you want to login instead? Press 'T' to try again or 'L' to login, 'E' to exit"  )
                if error == 't' or error == 'T':
                    Register()
                    break
                elif error == 'L' or error == 'l':
                    login()
                    break
                elif error == 'eL' or error == 'E':
                    exit(1)
        addUserInfo([user, hash_password(password)]) 
def login():
    pass

def addUserInfo(userinfo: list):
    pass

def sanitize(user):
    pass

def  userAlreadyExists(username, password):
    pass

def hash_password(password):
    return hashlib.sha256(str.encode)

def check_pasword_hash(password, hash):
    return hash_password(password) == hash