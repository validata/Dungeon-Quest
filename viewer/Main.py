from controller.Controller import *


class Main:
    def __init__(self):
        self.account_name = ""
        self.account_pw = ""
        self.character_id = 0
        self.character_name = ""
        self.dungeon_size = 0
        self.dungeon_corner = ""

    def menu_start(self):
        while True:
            print("Main Menu")
            choice = validate(["Login", "Signup", "Exit"])
            if not choice:
                self.menu_start()

            elif choice == 1:
                username = input("Enter username\n")
                password = input("Enter Password\n")
                if c.account_login(username, password):
                    print("Login ok")
                    if self.menu_character():
                        if self.menu_dungeon_start():
                            print("Battle ready to begin!")
                        else:
                            print("error1")
                    else:
                        print("error2")
                else:
                    print("Password incorrect")
                    self.menu_start()

            elif choice == 2:
                username = input("Enter new username:\n")
                password = input("Enter new password:\n")
                if c.account_create(username, password):
                    if c.account_login(username, password):
                        print("Acc created and logged in")
                        print("Please create your first char now")
                        if self.menu_character_new():
                            print("Char created!")
                            if self.menu_character():
                                print("Char menu")
                                if self.menu_dungeon_start():
                                    print("Dungeon settings created - LOAD THE GAME!")
                            else:
                                print("Failed")
                                self.menu_start()
                        else:
                            print("Error new char")

                    else:
                        print("Couldn't login")
                        self.menu_start()
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
            if choice == 1:
                character_existing = self.character_existing()          # User selects existing character
                if character_existing:
                    return True
                else:
                    print("Error selecting char")
                    return False
            if choice == 2:
                if self.menu_character_new():               # User creates new character
                    print("Successfully created character")
                    return True
                else:
                    print("Failure creating character")
                    return False
            return True
        else:
            clear_cmd()
            self.menu_character()

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
        clear_cmd()
        print("# Create Account #")
        account_name = input("Account Name: \n")
        account_pw = input("Account Password: \n")
        if c.account_create(account_name, account_pw):
            self.account_name = account_name
            self.account_pw = account_pw
            return True
        else:
            print("New account fail")
            return False

    def account_create_to_login(self):
        clear_cmd()
        if c.account_login(self.account_name, self.account_pw):
            print("Account created and logged in!\nUsername : " + str(self.account_name))
            print("Create your first character now:")
            return True
        else:
            print("Error trying to login!")
            return False

    def character_existing(self):
        clear_cmd()
        print("# Select a character #")
        # TODO GET REAL LIST OF CHARS
        character_list = c.character_list()
        if character_list:
            character_select_id = input("Select your character by ID:\n")
            if character_select_id:
                print("Selected character is: " + character_select_id)
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
        clear_cmd()
        print("# Create new character #")
        choice = validate(["Warrior", "Thief", "Wizard"])
        if choice:
            if choice == 1:
                print("Warrior born")
            elif choice == 2:
                print("Thief born")
            elif choice == 3:
                print("Wizard born")
            return True
        else:
            self.menu_character_new()
            print("Fix this if you see it!")
            return False

    def menu_dungeon_start(self):
        clear_cmd()
        print("# Dungeon Size #")
        choice_dungeon_size = validate(["Small", "Medium", "Large"])
        if choice_dungeon_size:
            if c.dungeon_size_set(choice_dungeon_size):
                print("Map size set" + str(self.dungeon_corner))
                choice_dungeon_corner = validate(["North West", "North East", "South West", "South East"])
                if choice_dungeon_corner:
                    self.dungeon_corner = choice_dungeon_corner
                    print("Corner set: " + str(self.dungeon_corner))
                    return True
                else:
                    print("error")
                    pass
            else:
                print("error")
                pass
        else:
            print("Not a valid size")
            self.menu_dungeon_start()

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
    print("\n" * 1)


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
            print("\nNot a valid number!")
            return False
        except TypeError:
            return False


if __name__ == '__main__':
    c = Controller()
    start = Main()
    start.menu_start()
