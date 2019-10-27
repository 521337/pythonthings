import pyperclip

Passwords = {}


def Newcredentials():
    print("Enter user:")
    User = input()
    print("Enter password:")
    Password = input()
    Passwords[User] = Password
    print("Password added to the database.")


def SearchDatabase():
    print("Enter the credentials user name:")
    Search = input()
    for x in Passwords.keys():
        if str(x) == Search:
            print("Found!")
            for y, z in Passwords.items():
                if x == y:
                    pyperclip.copy(z)
                    break
            print("Password of " + str(x) + " copied to paperclip.")
        else:
            print("Not found, returning to main menu")

while True:
    print("""\
Press 1 to enter new credentials.
Press 2 to search in database.
Press 3 to exit.\
""")
    whatToDo = input()
    if whatToDo == "1":
        Newcredentials()
        continue
    if whatToDo == "2":
        SearchDatabase()
        continue
    if whatToDo == "3":
        break
    else:
        print("This option is not valid. Please enter a valid option")
