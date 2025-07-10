LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z"]

UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
       "W", "X", "Y", "Z"]

DIGITS=["0","1","2","3","4","5","6","7","8","9"]

SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """,
 """, ",", ".", "<", ">", "?", "/", "`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    pass

def word_has_character(word, character_list):
    pass

def word_complexity(word):
    pass

def password_strength(password, min_length=10, strong_length=16):
    print(f"Checking password strength for: {password}")

def main():
    run = True

    while run:
        print("Password Strength Checker")
        password = input("Enter a password to check its strength, or enter (q/Q) to quit: ")

        if password.lower() == 'q':
            run = False
        else:
            password_strength(password)

if __name__ == "__main__":
    main()