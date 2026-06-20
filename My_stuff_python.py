import secrets
from random import randint
import sys
import os
import secrets
import string


def main():

    art= r"""
     /$$      /$$                  /$$$$$$   /$$                /$$$$$$   /$$$$$$ 
    | $$$    /$$$                 /$$__  $$ | $$               /$$__  $$ /$$__  $$
    | $$$$  /$$$$ /$$   /$$      | $$  \__//$$$$$$   /$$   /$$| $$  \__/| $$  \__/
    | $$ $$/$$ $$| $$  | $$      |  $$$$$$|_  $$_/  | $$  | $$| $$$$    | $$$$    
    | $$  $$$| $$| $$  | $$       \____  $$ | $$    | $$  | $$| $$_/    | $$_/    
    | $$\  $ | $$| $$  | $$       /$$  \ $$ | $$ /$$| $$  | $$| $$      | $$      
    | $$ \/  | $$|  $$$$$$$      |  $$$$$$/ |  $$$$/|  $$$$$$/| $$      | $$      
    |__/     |__/ \____  $$       \______/   \___/   \______/ |__/      |__/      
                /$$  | $$                                                       
                |  $$$$$$/                                                       
                \______/                                                        
    """


    while True:
        clear_terminal()

        print(art)    
        

        print("1 - FizzBuzz")
        print("2 - Guess the number")
        print("3 - Multiplication table")
        print("4 - Password generator")
        print("0 - Exit")

        k = get_int("\nYour choice: ", 0, 4)

        if k == 0:
            print("Goodbye then!")
            sys.exit()
        elif k == 1:
            clear_terminal()
            FizzBuzz()
        elif k == 2:
            clear_terminal()
            Guess_the_number()
        elif k == 3:
            clear_terminal()
            Multiplication_table()
        elif k == 4:
            clear_terminal()
            Password_generator()
        else:
            show_error()

def FizzBuzz():

    for i in range(1,101):
        if (i % 3 == 0 and i % 5 == 0):
            print(f"{i} - FizzBuzz")
        elif(i % 3 == 0):
            print(f"{i} - Fizz")
        elif(i % 5 == 0):
            print(f"{i} - Buzz")
        else:
            print(f"{i} - none")

    input("\nPress ENTER to continue")

    return

def Guess_the_number():

    number = randint(1, 100)
    attempts = 1

    print("Guess a number between 1 and 100")

    while True:
        guess = get_int("Your guess: ")         #Didn't use max and min number in get_int() because why not

        if guess < number:
            print("higher")
            attempts += 1

        elif guess > number:
            print("lower")
            attempts += 1

        else:
            print("\nYAAAY!!! YOU WON!!!")
            print(f"Your attempts: {attempts}")

            input("\nPress ENTER to continue")

            break

    return

def Multiplication_table():

    n = get_int("Choose a size of the table: ", min_value=1)         #Didn't use max and min number in get_int() because why should I restrict user?

    max_n = n*n

    width = len(str(max_n)) + 1

    for i in range(n):
        for j in range(n):
            print(f"{(i + 1) * (j + 1):>{width}}", end = "")

        print("")
    
    input("\nPress ENTER to continue")

    return

def Password_generator():

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special="!@#$%^&*()_-+=[]{}"
    alphabet = uppercase + lowercase + digits + special

    lenghth = get_int("How long should your password be (min = 4): ", min_value=4)

    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    all_chars = uppercase + lowercase + digits + special
    for _ in range(lenghth - 4):
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)

    print(f"\nYour new password is: {''.join(password)}, \n\nDon't forget it :)")

    input("\nPress ENTER to continue")

    return

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_error():
    print("Wrong choise, try again")
    input("\nPress ENTER to continue")
    return

def get_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            num = int(input(prompt))

            if min_value is not None and num < min_value:  # ← проверяем min_value, а не num
                print(f"Number must be >= {min_value}!\n")
                continue

            if max_value is not None and num > max_value:  # ← проверяем max_value, а не num
                print(f"Number must be <= {max_value}!\n")
                continue

            return num

        except ValueError:
            print("Enter a NUMBER, dumbass\n")

main()