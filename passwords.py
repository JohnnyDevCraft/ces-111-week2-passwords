"""
passwords.py - A password strength checker that evaluates the strength of a password based on its length and complexity.

Author: Johnathon Smith | CES111
Date: 2025-07-18

Enhancements:
- Added user interface improvements for better user experience.
- Allows users to change the minimum and strong length of passwords.
- Users can view current settings.
- Configured to work on both Windows and Unix-like systems.

Usage:
    python passwords.py

Notes:
    Not as nice as the original version I submitted, but this version does work from a single file.
    You can, however, view the original version in my GitHub Account:

    https://github.com/JohnnyDevCraft/ces-111-week2-passwords
"""

import os

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z"]

UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
       "W", "X", "Y", "Z"]

DIGITS=["0","1","2","3","4","5","6","7","8","9"]

SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """,
 """, ",", ".", "<", ">", "?", "/", "`", "~"]

MIN_LENGTH=10
STRONG_LENGTH=16

def word_in_file(word, filename, case_sensitive=False):
    file = open(filename, "r")
    if not case_sensitive:
        word = word.lower()
    for line in file:
        if not case_sensitive:
            line = line.lower()
        if word in line:
            file.close()
            return True
    file.close()
    return False

def word_has_character(word, character_list):
    for char in character_list:
        if char in word:
            return True
    return False

def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password):

    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    if len(password) < MIN_LENGTH:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= STRONG_LENGTH:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    complexity = word_complexity(password)
    return complexity + 1

def print_bar():
    print("=" * 50)

def print_empty_lines(lines=1):
    for _ in range(lines):
        print("\n")

def print_header(title="Welcome Page"):
    clear_screen()
    print_empty_lines()
    print(f"Password Strength Checker - {title}")
    print_bar()
    print_empty_lines()

def print_menu():
    print_header("Main  Menu")
    print("1. Check password strength")
    print("2. Change minimum length")
    print("3. Change strong length")
    print("4. View current settings")
    print("5. Exit")
    print_empty_lines()
    print_bar()
    print_empty_lines()
    return int(input("Choose an option: "))

def print_welcome():
    print_header("Welcome")
    print("Welcome to the Password Strength Checker! Designed by Johnathon Smith")
    print("This version has improved user expirience by allowing you to change the minimum and strong length of passwords.")
    print("It also has an improved menu system to make it easier to navigate the features.")

    print_empty_lines()
    input("Press ENTER to continue...")


def clear_screen():
    # Windows: cls, Unix-like: clear
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def print_settings():
    print_header("Current Settings")
    print(f"Minimum Length: {MIN_LENGTH}")
    print(f"Strong Length: {STRONG_LENGTH}")
    print_empty_lines()
    input("Press ENTER to continue...")

def set_min_length():
    global MIN_LENGTH
    print_header("Change Minimum Length")
    new_length = int(input(f"Current minimum length is {MIN_LENGTH}. Enter new minimum length: "))
    if new_length > 0:
        MIN_LENGTH = new_length
        print(f"Minimum length set to {MIN_LENGTH}.")
    else:
        print("Invalid length. Minimum length not changed.")
    input("Press ENTER to continue...")

def set_strong_length():
    global STRONG_LENGTH
    print_header("Change Strong Length")
    new_length = int(input(f"Current strong length is {STRONG_LENGTH}. Enter new strong length: "))
    if new_length > 0:
        STRONG_LENGTH = new_length
        print(f"Strong length set to {STRONG_LENGTH}.")
    else:
        print("Invalid length. Strong length not changed.")
    input("Press ENTER to continue...")

def check_password():
    print_header("Check Password Strength")
    password = input("Enter a password to check its strength: ")
    strength = password_strength(password)

    print(f"Password strength: {strength} (0 = not secure, 5 = very strong)\n")
    input("Press ENTER to continue...")




def main():
    while True:
        option = print_menu()
        if option == 1:
            check_password()
        elif option == 2:
            set_min_length()
        elif option == 3:
            set_strong_length()
        elif option == 4:
            print_settings()
        elif option == 5:
            print("Exiting the program. Goodbye!")
            input("Press ENTER to continue...")
            break
        else:
            print("Invalid option. Please try again.")
            input("Press ENTER to continue...")


if __name__ == "__main__":
    main()