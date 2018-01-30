from controller.Controller import *


class Main:
    def __init__(self):
        self.account_name = ""
        self.account_pw = ""
        self.character_id = 0
        self.character_name = ""
        self.character_class = ""
        self.dungeon_size = ""
        self.dungeon_corner = ""

    def menu_start(self):                                   # Start Menu
        while True:
            print("# Main Menu #")
            choice = validate(["Login", "Signup", "Exit"])  # Choices in menu
            if not choice:
                continue
                print("Debug error")

            elif choice == 1:                               # If user requests login
                if self.account_login():                    # Initiate login
                    if self.menu_character():               # Choices for characters (menu)
                        if self.menu_dungeon_start():       # Choices for dungeon start (menu)
                            print("Battle ready to begin!")
                        else:
                            print("Debug error 1")
                            continue
                    else:
                        print("Debug error 2")
                        continue
                else:
                    print("Login failed")
                    continue

            elif choice == 2:                               # If user wants to create new acc
                if self.account_create():                   # Initiate account create
                    if self.menu_character_new():           # Initiate new character and hero (menu)
                        if self.menu_character():           # Choices for characters (menu)
                            if self.menu_dungeon_start():   # Choices for dungeon start (menu)
                                print("Dungeon settings created - LOAD THE GAME!")
                            else:
                                print("Debug error3")
                                continue
                        else:
                            print("Debug error4")
                            continue
                    else:
                        print("Debug error5")
                        continue
                else:
                    print("Debug error6")
                    continue

            elif choice == 3:
                if menu_exit_program():
                    print("Exiting game")
                else:
                    continue

    def menu_character(self):                                       # Menu character
        while True:
            print("# Character Menu #")
            choice = validate(["Existing Character", "New Character"])
            if choice:
                clear_cmd()
                if choice == 1:                                     # If user want existing character
                    character_existing = self.character_existing()  # User selects in list of existing character
                    if character_existing:
                        return True
                    else:
                        print("Error selecting char")
                        return False
                elif choice == 2:                                   # If user want a new character
                    while True:
                        if self.menu_character_new():               # If func new character creating returns True
                            print("Character: " + self.character_name + ", Class: " + self.character_class + " was born!")
                            print("Preparing for battle.\n")
                            return True
                        else:
                            continue
            else:
                continue

    def menu_character_new(self):
        while True:
            print("# Create new character #")
            choice = validate(["Warrior", "Thief", "Wizard"])
            if choice:
                clear_cmd()
                if choice == 1:
                    self.character_class = "Warrior"
                elif choice == 2:
                    self.character_class = "Thief"
                elif choice == 3:
                    self.character_class = "Wizard"
                print("")
                return True
            else:
                continue

    def account_login(self):
        clear_cmd()
        print("# Account Login #")
        account_name = input("Account Name:\n")
        account_pw = input("Account Password:\n")
        if c.account_login(account_name, account_pw):
            self.account_name = account_name
            self.account_pw = account_pw
            clear_cmd()
            print("Login successful! Logged in with: " + self.account_name + "\n")
            return True
        else:
            print("Login failed")
            return False

    def account_create(self):
        print("# Create Account #")
        account_name = input("Account Name: \n")
        account_pw = input("Account Password: \n")
        if c.account_create(account_name, account_pw):
            self.account_name = account_name
            self.account_pw = account_pw
            clear_cmd()
            print("You have created the account " + self.account_name + "! \n")
            print("Please create your first char now:")
            if self.account_create_to_login():
                return True
            else:
                return False
        else:
            print("New account fail")
            return False

    def account_create_to_login(self):
        if c.account_login(self.account_name, self.account_pw):
            return True
        else:
            print("Error trying to login!")
            return False

    def character_existing(self):
        while True:
            print("# Select a character #")
            # TODO GET REAL LIST OF CHARS
            character_list = c.character_list()
            if character_list:
                character_select_id = input("Select your character by ID:\n")
                if character_select_id:
                    clear_cmd()
                    print("Selected character is: " + character_select_id + "\n")
                    return True
                else:
                    print("Try selecting again")
                    continue
            else:
                print("Failed fetching")
                continue

    def menu_dungeon_start(self):
        while True:
            print("# Dungeon Size #")
            choice_dungeon_size = validate(["Small", "Medium", "Large"])
            if choice_dungeon_size:
                if choice_dungeon_size == 1:
                    self.dungeon_size = "Small"
                elif choice_dungeon_size == 2:
                    self.dungeon_size = "Medium"
                elif choice_dungeon_size == 3:
                    self.dungeon_size = "Large"
                clear_cmd()
                print("Dungeon size set: " + str(self.dungeon_size) + "\n")
                c.dungeon_size = choice_dungeon_size
                choice_dungeon_corner = validate(["North West", "North East", "South West", "South East"])
                if choice_dungeon_corner:
                    if choice_dungeon_corner == 1:
                        self.dungeon_corner = "North West"
                    elif choice_dungeon_corner == 2:
                        self.dungeon_corner = "North East"
                    elif choice_dungeon_corner == 3:
                        self.dungeon_corner = "South West"
                    elif choice_dungeon_corner == 4:
                        self.dungeon_corner = "South East"
                    clear_cmd()
                    print("Dungeon size: " + str(self.dungeon_size))
                    print("Dungeon corner: " + str(self.dungeon_corner) + "\n")
                    return True
                else:
                    print("There are only four corners!")
                    continue
            else:
                print("Not a valid size")
                continue


def menu_exit_program():
    while True:
        clear_cmd()
        quit_confirm = input("User requesting to quit game. Confirm with Y/N:\n ")
        clear_cmd()
        if quit_confirm.lower() == 'y':
            print("\nQuitting game. Bye!")
            raise SystemExit
        elif quit_confirm.lower() == 'n':
            return False
        else:
            continue


def clear_cmd():
    print("*clearing window*" + "\n" * 3)


def validate(menu_choices):
    while True:
        try:
            for i, choice in enumerate(menu_choices):
                print(str(i + 1) + ". " + choice)
            choice = input()
            choice = int(choice)
            if 0 < choice <= len(menu_choices):
                return choice
            else:
                raise ValueError
        except ValueError:
            clear_cmd()
            print("\nNot a valid choice!\n")
            return False
        except TypeError:
            return False


if __name__ == '__main__':
    c = Controller()
    start = Main()
    start.menu_start()

