class Constants:
    """
    This class contains constants used throughout the application.
    """

    # Constants for the application
    LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]

    UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]

    DIGITS=["0","1","2","3","4","5","6","7","8","9"]

    SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """,
     """, ",", ".", "<", ">", "?", "/", "`", "~"]

    DICTIONARY_FILE = "wordlist.txt"

    COMMON_PASSWORDS_FILE = "toppasswords.txt"

    MENU_OPTIONS = {
        "check": "Check Password Strength",
        "set-min": "Set Minimum Password Length",
        "set-strong": "Set Strong Password Length",
        "reset": "Reset Settings",
        "generate": "Generate Password",
        "quit": "Exit"
    }

    MENU_OPTIONS_ARRAY = list(MENU_OPTIONS.values())
