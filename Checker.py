from Constants import *
from Settings import Settings
class Checker:
    def __init__(self, settings: Settings):
        self.settings = settings

    def word_in_file(self, word, filename, case_sensitive=False):
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

    def word_has_character(self, word, character_list):
        for char in character_list:
            if char in word:
                return True
        return False

    def word_complexity(self, word):
        complexity = 0
        if self.word_has_character(word, Constants.LOWER):
            complexity += 1
        if self.word_has_character(word, Constants.UPPER):
            complexity += 1
        if self.word_has_character(word, Constants.DIGITS):
            complexity += 1
        if self.word_has_character(word, Constants.SPECIAL):
            complexity += 1
        return complexity

    def password_strength(self, password, min_length=10, strong_length=16):

        if self.word_in_file(password, Constants.DICTIONARY_FILE, case_sensitive=False):
            print("Password is a dictionary word and is not secure.")
            return 0

        if self.word_in_file(password, Constants.COMMON_PASSWORDS_FILE, case_sensitive=True):
            print("Password is a commonly used password and is not secure.")
            return 0

        if len(password) < self.settings.min_length:
            print("Password is too short and is not secure.")
            return 1

        if len(password) >= self.settings.strong_length:
            print("Password is long, length trumps complexity this is a good password.")
            return 5

        complexity = self.word_complexity(password)
        return complexity + 1

    def check_password(self):
        password = input("Enter a password to check its strength: ")
        strength = self.password_strength(password)
        print(f"Password strength: {strength} (0 = not secure, 5 = very strong)\n")
        input("Press ENTER to continue...")