from pathlib import Path
import os


def readfileandfolder():
    path = Path("")
    items = list(path.rglob("*"))

    for i, item in enumerate(items):
        print(f"{i + 1} : {item}")


# Creating a file
def createfile():
    try:
        readfileandfolder()

        name = input("Enter the file name: ")
        p = Path(name)

        if not p.exists():
            with open(p, "w") as f:
                data = input("Enter the data you want to write inside the file: ")
                f.write(data)

            print("FILE CREATED SUCCESSFULLY")
        else:
            print("File already exists")

    except Exception as err:
        print(f"Error occurred: {err}")


# Reading a file
def readfile():
    try:
        readfileandfolder()

        name = input("Enter the file name: ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, "r") as f:
                data = f.read()
                print(data)
        else:
            print("File does not exist")

    except Exception as err:
        print(f"Error occurred: {err}")


# Updating a file
def updatefile():
    try:
        readfileandfolder()

        name = input("Enter the file name: ")
        p = Path(name)

        if p.exists() and p.is_file():

            print("Enter 1 for changing your file name")
            print("Enter 2 for overwriting your file content")
            print("Enter 3 for appending content in your file")

            res = int(input("Please enter your choice: "))

            if res == 1:
                name2 = input("Enter the new file name: ")
                p2 = Path(name2)
                p.rename(p2)

                print("Renamed successfully")

            if res == 2:
                with open(p, "w") as f:
                    data = input("Enter the new data which you want to overwrite: ")
                    f.write(data)

                print("File overwriting completed")

            if res == 3:
                with open(p, "a") as f:
                    data = input("Enter the new data which you want to append: ")
                    f.write(" " + data)

                print("Appending completed")

        else:
            print("File does not exist")

    except Exception as err:
        print(f"Error occurred: {err}")


# Deleting a file
def deletefile():
    try:
        readfileandfolder()

        name = input("Enter the file name: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("Deletion completed")
        else:
            print("File does not exist")

    except Exception as err:
        print(f"Error occurred: {err}")


# Main Menu
print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

user_response = int(input("Enter your response: "))

if user_response == 1:
    createfile()
elif user_response == 2:
    readfile()
elif user_response == 3:
    updatefile()
elif user_response == 4:
    deletefile()