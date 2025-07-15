LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z"]

UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
       "W", "X", "Y", "Z"]

DIGITS=["0","1","2","3","4","5","6","7","8","9"]

SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """,
 """, ",", ".", "<", ">", "?", "/", "`", "~"]

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

def password_strength(password, min_length=10, strong_length=16):

    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    complexity = word_complexity(password)
    return complexity + 1



def main():
    while True:
        print("Password Strength Checker")
        password = input("Enter a password to check its strength, or enter (q/Q) to quit: ")
        strength = 0

        if password.lower() == 'q':
            exit()
        else:
            strength = password_strength(password)

        print(f"Password strength: {strength} (0 = not secure, 5 = very strong)\n")

if __name__ == "__main__":
    main()