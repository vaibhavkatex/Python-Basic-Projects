#Import Moduals 

import math
import random
from datetime import datetime

#create a Dictionary
history = {}

# Create a Function def arithmetic():
def arithmetic():
    try:
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter Choice: ")

        if choice == "1":
            result = a + b
        elif choice == "2":
            result = a - b
        elif choice == "3":
            result = a * b
        elif choice == "4":
            result = a / b
        else:
            print("Invalid Choice")
            return

        print("Result:", result)
        history[str(datetime.now())] = result

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except ValueError:
        print("Invalid Input!")

# Creating a Function def scientific():
def scientific():
    try:
        num = float(input("Enter Number: "))
        print("Square Root:", math.sqrt(num))
        history[str(datetime.now())] = math.sqrt(num)

    except ValueError:
        print("Invalid Input!")

# Creating a Function def random_numbers():
def random_numbers():
    nums = random.sample(range(1, 101), 5)
    print("Random Numbers:", nums)
    history[str(datetime.now())] = nums

# Creating a Function def view_history():
def view_history():
    if len(history) == 0:
        print("No History Available.")
    else:
        print("\nHistory:")
        for time, result in history.items():
            print(time, ":", result)

# main Menu
while True:
    print("\n----- Smart Calculator -----")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculation")
    print("3. Generate Random Numbers")
    print("4. View History")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        arithmetic()

    elif choice == "2":
        scientific()

    elif choice == "3":
        random_numbers()

    elif choice == "4":
        view_history()

    elif choice == "5":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")