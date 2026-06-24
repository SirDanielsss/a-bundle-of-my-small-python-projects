import sys
import os

import secrets
import string

from datetime import datetime
from random import randint


def main():
    """Main menu loop - displays ASCII art and navigation options."""

    art = r"""
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

        # Menu options dictionary
        things = {
            "1": "FizzBuzz",
            "2": "Guess the number",
            "3": "Multiplication table",
            "4": "Passwords",
            "5": "Todo list",
            "0": "Exit"
        }

        for thing in things:
            print(thing, things[thing], sep=" - ")

        # Get valid numeric choice from user
        k = get_int("\nYour choice: ", 0, len(things) - 1)

        # Route to appropriate function based on choice
        if k == 0:
            print("\nGoodbye then!")
            sys.exit()
        elif k == 1:
            fizz_buzz()
        elif k == 2:
            guess_the_number()
        elif k == 3:
            multiplication_table()
        elif k == 4:
            passwords()
        elif k == 5:
            todo_list()
        else:
            show_error()


def fizz_buzz():
    """Classic FizzBuzz problem: prints 1-100 with Fizz/Buzz/FizzBuzz replacements."""
    clear_terminal()

    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print(f"{i} - FizzBuzz")
        elif (i % 3 == 0):
            print(f"{i} - Fizz")
        elif (i % 5 == 0):
            print(f"{i} - Buzz")
        else:
            print(f"{i} - none")

    input("\nPress ENTER to continue")


def guess_the_number():
    """Number guessing game: user tries to guess a random number between 1-100."""
    clear_terminal()
    print("=== guessing the number ===\n")

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


def multiplication_table():
    """Generates a multiplication table of user-specified size."""
    clear_terminal()
    print("=== multiplication table ===\n")

    n = get_int("Choose a size of the table: ", min_value=1)
    max_n = n * n
    width = len(str(max_n)) + 1  # Calculate padding for alignment

    for i in range(n):
        for j in range(n):
            print(f"{(i + 1) * (j + 1):>{width}}", end="")
        print("")

    input("\nPress ENTER to continue")


# ──────────────────────── PASSWORD FUNCTIONS ──────────────────────── #

def passwords():
    """Password submenu: generate passwords, view history, or delete entries."""
    while True:
        clear_terminal()
        print("=== passwords ===\n")
        password_history()

        print("1 - Generate a password")
        print("2 - Delete passwords")
        print("0 - Exit")

        k = get_int("Your choice: ", 0, 2)

        if k == 1:
            clear_terminal()
            password_generator()
        elif k == 2:
            delete_password()
        elif k == 0:
            break


def load_passwords():
    """Load all passwords from file into a list (one entry per line)."""
    try:
        with open("Passwords.txt", "r") as file:
            return [line.rstrip('\n') for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_passwords(passwords_list):
    """Write a list of password strings to the file (overwrites)."""
    with open("Passwords.txt", "w") as file:
        for pwd in passwords_list:
            file.write(pwd + "\n")


def save_password(password):
    """Append a single password to the file with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H")
    with open("Passwords.txt", 'a') as file:
        file.write(f"[{timestamp}] {password}\n")


def password_generator():
    """Generate a secure random password with at least 4 characters."""
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = r"!@#$%^&*()_-+=[]{}"
    all_chars = uppercase + lowercase + digits + special

    length = get_int("How long should your password be (min = 4): ", min_value=4)

    # Ensure at least one character from each category
    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    # Fill remaining length with random characters from all categories
    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)
    password = ''.join(password)

    save_password(password)

    print("=== password generator ===\n")
    print(f"\nYour new password is: {password}\n\nWrote in the Passwords.txt file :)")
    input("\nPress ENTER to continue")


def password_history():
    """Display all saved passwords from file."""
    passwords = load_passwords()
    if not passwords:
        print("You don't have any generated passwords yet\n")
    else:
        for pwd in passwords:
            print(pwd)
        print()


def delete_password():
    """Delete passwords: accepts a number, 'all', or blank (cancel)."""
    while True:
        clear_terminal()
        print("=== delete passwords ===\n")

        passwords = load_passwords()
        if not passwords:
            print("No passwords saved yet.\n")
            input("Press ENTER to continue")
            return

        # Display passwords with numbers for selection
        for i, pwd in enumerate(passwords, start=1):
            print(f"{i}: {pwd}")
        print()

        # Accept string input for flexible deletion options
        choice = input("Enter a number, 'all' to delete everything, or ENTER to exit: ").strip()

        if choice == "":
            # Blank input = cancel
            break
        elif choice.lower() == "all":
            # Delete everything with confirmation
            confirm = input("Are you sure you want to delete ALL passwords? (y/n): ").strip().lower()
            if confirm == "y":
                save_passwords([])
                print("All passwords deleted.\n")
                input("Press ENTER to continue")
            break
        else:
            # Try to interpret input as a number
            try:
                num = int(choice)
                if 1 <= num <= len(passwords):
                    passwords.pop(num - 1)
                    save_passwords(passwords)
                    print(f"Password {num} deleted.\n")
                    input("Press ENTER to continue")
                    break
                else:
                    print(f"Number must be between 1 and {len(passwords)}.")
                    input("Press ENTER to continue")
            except ValueError:
                print("Invalid input. Please enter a number, 'all', or leave blank.")
                input("Press ENTER to continue")


# ──────────────────────── TODO LIST FUNCTIONS ──────────────────────── #

def todo_list():
    """Todo list submenu: view, add, or delete tasks."""
    while True:
        clear_terminal()
        print("=== todo list ===\n")
        view_tasks()

        print("1 - Write a new task")
        print("2 - Delete a task")
        print("0 - Exit")

        k = get_int("\nYour choice: ", 0, 2)

        if k == 1:
            add_task()
        elif k == 2:
            delete_task()
        elif k == 0:
            break


def load_tasks():
    """Load all tasks from file into a list (raw text, no numbering)."""
    try:
        with open("Todo.txt", 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Write a list of task strings to file (one per line, no numbering in file)."""
    with open("Todo.txt", 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")


def view_tasks():
    """Display all tasks with numbers for selection."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet\n")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}: {task}")
        print()


def add_task():
    """Add a new task to the list. Blank input cancels."""
    while True:
        text = input("Enter a task (leave blank to exit): ")

        if text == "":
            break
        else:
            tasks = load_tasks()
            tasks.append(text)
            save_tasks(tasks)
            break


def delete_task():
    """Delete tasks: accepts a number, 'all', or blank (cancel)."""
    while True:
        clear_terminal()
        print("=== delete task ===\n")

        tasks = load_tasks()
        if not tasks:
            print("No tasks to delete\n")
            input("Press ENTER to continue")
            return

        # Display tasks with numbers for selection
        for i, task in enumerate(tasks, start=1):
            print(f"{i}: {task}")
        print()

        # Accept string input for flexible deletion options
        choice = input("Enter a number, 'all' to delete everything, or ENTER to exit: ").strip()

        if choice == "":
            # Blank input = cancel
            break
        elif choice.lower() == "all":
            # Delete everything with confirmation
            confirm = input("Are you sure you want to delete ALL tasks? (y/n): ").strip().lower()
            if confirm == "y":
                save_tasks([])  # Write empty list to file
                print("All tasks deleted.\n")
                input("Press ENTER to continue")
            break
        else:
            # Try to interpret input as a number
            try:
                num = int(choice)
                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"Task {num} deleted.\n")
                    input("Press ENTER to continue")
                    break
                else:
                    print(f"Number must be between 1 and {len(tasks)}.")
                    input("Press ENTER to continue")
            except ValueError:
                print("Invalid input. Please enter a number, 'all', or leave blank.")
                input("Press ENTER to continue")


# ──────────────────────── UTILITY FUNCTIONS ──────────────────────── #

def clear_terminal():
    """Clear terminal screen (cross-platform: Windows and Unix)."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def show_error():
    """Display generic error message for invalid menu choices."""
    print("Wrong choice, try again")
    input("\nPress ENTER to continue")


def get_int(prompt, min_value=None, max_value=None):
    """
    Get a validated integer from the user.

    Args:
        prompt: Message to display to user
        min_value: Minimum acceptable value (inclusive), or None for no limit
        max_value: Maximum acceptable value (inclusive), or None for no limit

    Returns:
        Validated integer from user
    """
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


# ──────────────────────── ENTRY POINT ──────────────────────── #

main()