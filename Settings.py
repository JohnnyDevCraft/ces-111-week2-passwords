class Settings:
    def __init__(self):
        self.min_length = 10
        self.strong_length = 16

    def set_min_length(self):
        length = int(input("Enter the minimum password length (default is 10): "))
        if length < 1:
            raise ValueError("Minimum length must be at least 1.")
        self.min_length = length

    def set_strong_length(self):
        length = int(input("Enter the strong password length (default is 16): "))
        if length < self.min_length:
            raise ValueError("Strong length must be greater than or equal to minimum length.")
        self.strong_length = length

    def get_length_settings(self):
        return {
            "min_length": self.min_length,
            "strong_length": self.strong_length
        }

    def reset_settings(self):
        print("Resetting settings to default values.")
        self.__init__()
        print("Settings have been reset to default values.")
        input("Press ENTER to continue...")