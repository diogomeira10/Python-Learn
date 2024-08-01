# The point of this program is to store and manage personal passwords 

#The passwords are going to be encripted

## 'pass' is used as a placeholder for future code

## using the 'with', as soon as the operations in the file are done the file closes automatically, no need for the file.close()

## 'rstrip' removes every space at the end of the string

## 'encode' turns str into bytes 

'''
    Multiline comment in Python
'''

from cryptography.fernet import Fernet

def load_key():
    file = open('key.key','rb')
    key = file.read()
    return key

# print('This is the original key', key)
# print('This is the encripted key', fer)

master_pwd = input("What is the master password?")

key = load_key() + master_pwd.encode()
print(key)
fer = Fernet(key)

'''def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

write_key()'''


def view():
    file = open('passwords.txt','r')
    for l in file.readlines():
        data = l.rstrip()
        user, password = data.split('|')
        print(f'User: {user},password:{fer.decrypt(password.encode())}')
    file.close()


def add():

    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt','a') as file: ## first argument is the name of the file, the second is the mode I want to apply to that file.
        file.write(f'{name} | {fer.encrypt(pwd.encode()).decode()}\n')



while True:

    mode = input("Would you like to add a new password or view existing ones (view,add), press q to quit?").lower()

    if mode == 'q':        
        quit()


    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid Mode')
        continue 