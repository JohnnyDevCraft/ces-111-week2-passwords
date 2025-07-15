from pythonclimenu import menu
from Settings import Settings
from Checker import Checker
from Constants import Constants

class App:
    def __init__(self):
        self.settings = Settings()
        self.checker = Checker(self.settings)

    def print_header(self):
        print("Password Strength Checker")
        print("This application checks the strength of passwords based on various criteria.")
        print("You can also adjust settings for minimum and strong password lengths.\n")
        input("Press enter to begin...")
        self.run_menu()

    def print_exit_message(self):
        print("Thank you for using the Password Strength Checker!")
        print("Goodbye!\n")

    def run_menu(self):

        while True:
            choice = menu(
                title="Password Strength Checker",
                options = Constants.MENU_OPTIONS_ARRAY,
                cursor_color="blue"
            )

            if choice == Constants.MENU_OPTIONS["check"]:
                self.checker.check_password()
            elif choice == Constants.MENU_OPTIONS["set-min"]:
                try:
                    self.settings.set_min_length()
                except ValueError as e:
                    print(f"Error: {e}")
            elif choice == Constants.MENU_OPTIONS["set-strong"]:
                try:
                    self.settings.set_strong_length()
                except ValueError as e:
                    print(f"Error: {e}")
            elif choice == Constants.MENU_OPTIONS["reset"]:
                self.settings.reset_settings()
            elif choice == Constants.MENU_OPTIONS["generate"]:
                print("Password generation feature is not implemented yet.")
                input("Press ENTER to continue...")
            elif choice == Constants.MENU_OPTIONS["quit"]:
                self.print_exit_message()
                break


    def run(self):
        self.print_header()

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()