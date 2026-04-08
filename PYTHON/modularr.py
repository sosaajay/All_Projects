import time
import random
import uuid
import math
from datetime import datetime

def datetime_menu():
    while True:
        print("\n1. Show Current Date & Time")
        print("2. Countdown Timer")
        print("3. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            now = datetime.now()
            print("Current Date & Time:", now)

        elif ch == "2":
            sec = int(input("Enter seconds: "))
            while sec > 0:
                print(sec)
                time.sleep(1)
                sec -= 1
            print("Time's Up!")

        elif ch == "3":
            break
        else:
            print("Invalid Choice!")

def math_menu():
    while True:
        print("\n1. Factorial")
        print("2. Compound Interest")
        print("3. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            n = int(input("Enter number: "))
            print("Factorial:", math.factorial(n))

        elif ch == "2":
            p = float(input("Principal: "))
            r = float(input("Rate: "))
            t = float(input("Time (years): "))
            amount = p * (1 + r/100)**t
            print("Amount:", amount)

        elif ch == "3":
            break
        else:
            print("Invalid Choice!")


def random_menu():
    while True:
        print("\n1. Random Number")
        print("2. Random Password")
        print("3. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            print("Random Number:", random.randint(1, 100))

        elif ch == "2":
            length = int(input("Length: "))
            chars = "abcABC123@#$"
            pwd = ""
            for i in range(length):
                pwd += random.choice(chars)
            print("Password:", pwd)

        elif ch == "3":
            break
        else:
            print("Invalid Choice!")

def file_menu():
    while True:
        print("\n1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            name = input("File name: ")
            open(name, "w").close()
            print("File Created!")

        elif ch == "2":
            name = input("File name: ")
            text = input("Enter text: ")
            f = open(name, "w")
            f.write(text)
            f.close()
            print("Written!")

        elif ch == "3":
            name = input("File name: ")
            f = open(name, "r")
            print(f.read())
            f.close()

        elif ch == "4":
            name = input("File name: ")
            text = input("Enter text: ")
            f = open(name, "a")
            f.write("\n" + text)
            f.close()
            print("Appended!")

        elif ch == "5":
            break
        else:
            print("Invalid Choice!")

while True:
    print("\n========= Multi Utility Toolkit =========")
    print("1. Datetime & Time")
    print("2. Math Operations")
    print("3. Random Tools")
    print("4. Generate UUID")
    print("5. File Operations")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        datetime_menu()
    elif choice == "2":
        math_menu()
    elif choice == "3":
        random_menu()
    elif choice == "4":
        print("UUID:", uuid.uuid4())
    elif choice == "5":
        file_menu()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid Choice!")
