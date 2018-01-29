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

    def menu_start(self):
        while True:
            print("# Main Menu #")
            choice = validate(["Login", "Signup", "Exit"])
            if not choice:
                self.menu_start()

            elif choice == 1:
                clear_cmd()
                if self.account_login():
                    clear_cmd()
                    if self.menu_character():
                        if self.menu_dungeon_size():
                                if self.menu_dungeon_corner():
                                    print("Battle ready to begin!")
                                else:
                                    print("error2")
                        else:
                            print("error1")
                    else:
                        print("Login failed")
                else:
                    print("Password incorrect")
                    self.menu_start()

            elif choice == 2:
                if self.account_create():
                    clear_cmd()
                    if self.menu_character_new():
                        print("Char created!")
                        if self.menu_character():
                            print("Char menu")
                            if self.menu_dungeon_size():
                                print("Size menu?")
                                if self.menu_dungeon_corner():
                                    print("Dungeon settings created - LOAD THE GAME!")
                                else:
                                        print("Failed")
                                        self.menu_start()
                            else:
                                print("Failed on size")
                                self.menu_start()
                    else:
                        print("Error new char")
                        self.menu_character_new()
                        print("After error new char")
                else:
                    print("Try again")
                    self.menu_start()

            elif choice == 3:
                print("Exit")
                self.menu_exit_program()

    def menu_character(self):                                           # Menu character
        print("# Character Menu #")
        choice = validate(["Existing Character", "New Character"])
        if choice:
            clear_cmd()
            if choice == 1:
                character_existing = self.character_existing()          # User selects existing character
                if character_existing:
                    return True
                else:
                    print("Error selecting char")
                    return False
            if choice == 2:
                if self.menu_character_new():
                    print("Character: " + self.character_name + ", Class: " + self.character_class + " was born!")
                    print("Preparing for battle.\n")
                    return True
                else:
                    print("Failure creating character")
                    return False
            return True
        else:
            clear_cmd()
            "No choice"
            self.menu_character()

    def account_login(self):
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
                clear_cmd()
                print("Try selecting again")
                self.character_existing()
            return True
        else:
            print("Failed fetching")
            return False

    def menu_character_new(self):
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
            print("Else in menu character new")
            print("Fix this if you see it!")
            return False

    def menu_dungeon_size(self):
        print("# Select Dungeon Size #")
        choice_dungeon_size = validate(["Small Dungeon", "Medium Dungeon", "Large Dungeon"])
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
            return True

        else:
            print("Not a valid size")
            self.menu_dungeon_size()

    def menu_dungeon_corner(self):
        print("# Select Entrypoint to the Dungeon #")
        choice_dungeon_corner = validate(["North Western Sewers", "North Eastern Gate", "South Western Trapdoor", "South Eastern Narrow Passage"])
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
            print("You have chosen " + str(self.dungeon_corner) + "\n")
            c.dungeon_corner = choice_dungeon_corner
            return True
        else:
            print("There are only four corners!")
            self.menu_dungeon_corner()
        #"Character: " + self.character_name + ", Class: " + self.character_class + " was born!")

    def menu_exit_program(self):
        clear_cmd()
        quit_confirm = input("User requesting to quit game. Confirm with Y/N:\n ")
        clear_cmd()
        if quit_confirm.lower() == 'y':
            print("\nQuitting game. Bye!")
            raise SystemExit
        elif quit_confirm.lower() == 'n':
            self.menu_start()


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
            print("\nNot a valid number!\n")
            return False
        except TypeError:
            return False


if __name__ == '__main__':
    c = Controller()
    start = Main()
    start.menu_start()

