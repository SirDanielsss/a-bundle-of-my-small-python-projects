import sys
import os

import secrets
import string

from datetime import datetime
from random import randint


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
        
        things = {
            "1": "FizzBuzz",
            "2": "Guess the number",
            "3": "Multiplication table",
            "4": "Password generator",
            "5": "Password history",
            "0": "Exit"
        }

        for thing in things:
            print(thing, things[thing], sep=" - ")


        k = get_int("\nYour choice: ", 0, len(things)-1)

        if k == 0:
            print("\nGoodbye then!")
            sys.exit()
        elif k == 1:
            clear_terminal()
            fizz_buzz()
        elif k == 2:
            clear_terminal()
            guess_the_number()
        elif k == 3:
            clear_terminal()
            multiplication_table()
        elif k == 4:
            clear_terminal()
            password_generator()
        elif k == 5:
            clear_terminal()
            password_history()
        else:
            show_error()

def fizz_buzz():

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

def guess_the_number():

    number = randint(1, 100)
    attempts = 1

    print("Guess a number between 1 and 100")

    while True:
        guess = get_int("Your guess: ")

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

def multiplication_table():

    n = get_int("Choose a size of the table: ", min_value=1)

    max_n = n*n

    width = len(str(max_n)) + 1

    for i in range(n):
        for j in range(n):
            print(f"{(i + 1) * (j + 1):>{width}}", end = "")

        print("")
    
    input("\nPress ENTER to continue")

    return

def password_generator():

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special=r"!@#$%^&*()_-+=[]{}"
    all_chars = uppercase + lowercase + digits + special

    length = get_int("How long should your password be (min = 4): ", min_value=4)

    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]
    
    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)

    password = ''.join(password)
    
    save_password(password)

    print(f"\nYour new password is: {password}\n\nWrote in the Passwords.txt file :)")

    input("\nPress ENTER to continue")

    return

def password_history():
    try:
        with open("Passwords.txt", "r") as file:
            content = file.read()
            if content.strip():
                print("=== Your passwords ===")
                print(content)
                print("1 - delete history")
                print("0 - exit\n")
                
                choice = get_int("Your choice: ", 0, 1)
                
                if choice == 0:
                    return
                elif choice == 1:
                    delete_password_history()
            else:
                print("You don't have any generated passwords yet\n")
                
    except FileNotFoundError:
        print("You don't have any generated passwords yet\n")
    
    input("Press ENTER to continue")   




def save_password(password):


    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("Passwords.txt", 'a') as file:
        file.write(f"[{timestamp}] {password}\n")

def delete_password_history():

    file_path = "Passwords.txt"
    try:
        os.remove(file_path)
        print(f"File {file_path} has been deleted\n")
    except FileNotFoundError:
        print(f"File {file_path} already doesn't exist\n")

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

            if min_value is not None and num < min_value:
                print(f"\nNumber must be >= {min_value}!")
                continue

            if max_value is not None and num > max_value:
                print(f"\nNumber must be <= {max_value}!")
                continue

            return num

        except ValueError:
            print("\nEnter a NUMBER")
            continue

main()