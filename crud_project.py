from pathlib import Path
import os


def readfileandfolder():
    path = Path('')
    items = list(path.rglob("*"))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


def creatfile():
    try:
        readfileandfolder()
        name = input("please tell your file name:- ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("what you want to write in this file:- ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        else:
            print("this file already exists")
    except Exception as err:
        print(f"An error occurred as {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("which file you want to read:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            print("Read successfully")
        else:
            print("the file does not exist")
    except Exception as err:
        print(f"An error occurred as {err}")


def updatefile():
    try:
        readfileandfolder()
        name = input("tell which file you want to update:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file")
            print("press 2 for overwriting the data of your file")
            print("press 3 for appending some content to your file")

            res = int(input("tell your response:- "))

            if res == 1:
                name2 = input("tell your new file name:- ")
                p2 = Path(name2)
                p.rename(p2)
                print("file renamed successfully")

            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("what you want to write (this will overwrite data):- ")
                    fs.write(data)
                print("file overwritten successfully")

            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("tell what you want to append:- ")
                    fs.write(data)
                print("content appended successfully")

            else:
                print("invalid option")
        else:
            print("the file does not exist")
    except Exception as err:
        print(f"An error occurred as {err}")


def deletefile():
    try:
        readfileandfolder()
        name = input("which file you want to delete:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("file removed successfully")
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An error occurred as {err}")


while True:
    print("\npress 1 for creating a file")
    print("press 2 for reading a file")
    print("press 3 for updating a file")
    print("press 4 for deleting a file")
    print("press 5 to exit")

    try:
        check = int(input("please tell your response:- "))
    except ValueError:
        print("please enter a number")
        continue

    if check == 1:
        creatfile()
    elif check == 2:
        readfile()
    elif check == 3:
        updatefile()
    elif check == 4:
        deletefile()
    elif check == 5:
        print("Goodbye!")
        break
    else:
        print("invalid choice")