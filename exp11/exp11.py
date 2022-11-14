# make a file1.txt with some text inside, before running the program

import os

while True:
    print("1. Read a file and copy it to another")
    print("2. Append to an existing file")
    print("3. Count Details of the file")
    print("4. Display all files and directories in current directory")
    print("5. Exit")
    choice = int(input("Enter a choice: "))

    if choice == 1:
        with open("file1.txt", "r") as file1:
            data = file1.read()
            print("file1.txt: \n", data)
            with open("file2.txt", "w+") as file2:
                file2.write(data)
                file2.seek(0)
                print("file2.txt: \n", file2.read())

    elif choice == 2:
        with open("file3.txt", "a+") as file3:
            append_data = input("Enter data to append: ")
            file3.write(append_data)
            file3.seek(0)
            print("file3.txt: \n", file3.read())

    elif choice == 3:
        with open("file3.txt", "r") as file3:
            data = file3.read()
            file3.seek(0)
            lines = len(file3.readlines())
            words = len(data.split())
            characters = len(data)
            print(f" Lines = {lines} \n Words = {words} \n Characters = {characters}")

    elif choice == 4:
        for f in os.listdir():
            if os.path.isfile(f):
                print("file: ", f)
            else:
                print("folder: ", f)

    elif choice == 5:
        break
