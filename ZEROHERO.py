#!/bin/python3.7
import pyperclip

Passwords = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6'}


def SearchInDictByKey(key, dict):
    # if len(dict) == 0:
    #     return 0
    for x in dict.keys():
        if str(x) != key:
            return 1
        if str(x) == key:
            for y, z in dict.items():
                if x == y:
                    return str(z)

print("Programm to store user and passwords (insecure). Everything you do here is not permanent. Have fun.")
while True:
    print('''\


Press 1 to exit.

Press 2 to add credentials to database.
''')
    if len(Passwords) != 0:
        print('''Press 3 to search in database.''')
    whatToDo = input()
    if whatToDo == "1":
        break
    if whatToDo == "2":
        print("Enter username:")
        User = input()
        print("Enter password:")
        Password = input()
        Passwords[User] = Password
        print("Password added to the database.")
        continue
    if whatToDo == "3":
        print("Enter the credentials user name:")
        Search = input()
        Key = SearchInDictByKey(Search, Passwords)
        if Key == 1:
            print("Not found.")
            continue
        else:
            pyperclip.copy(Key)
            print("Password of \"" + Search + "\" copied to paperclip.")
            continue

    else:
        print("This option is not valid. Please enter a valid option")

# TODO:
# 1. Poder añadir varias entradas con el mismo nombre.
# 2. Generador de contraseñas aleatroias.
#
