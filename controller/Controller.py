

class Controller:
    def __init__(self):
        self.account = None     # Account object
        self.account_id = 1
        self.account_pw = 2
        self.account_name = "Account name"
        self.character = None   # Character object
        self.character_id = 1
        self.character_name = "Character Name"
        self.character_hero = "Warrior"
        self.dungeon_size = 0
        self.dungeon_corner = ""

    def account_create(self, account_name, account_pw):
        try:
            # TODO Generate auto incremental ID too
            self.account_name = account_name
            self.account_pw = account_pw
            # TODO Send to Database and if succeed return True
            return True
        except (TypeError, ValueError) as e:
            print(e)
            return False

    def account_login(self, account_name, account_pw):
        try:
            # TODO Login try to DB, if True procceed
            if True:
                self.account_name = account_name
                self.account_pw = account_pw
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
        
    def character_create(self, character_name, character_hero):
        # TODO Generateu auto inc ID
        self.character_name = character_name
        self.character_hero = character_hero
        print("Char created: ")
        print(self.character_name)
        print(self.character_hero)

    def character_login(self, character_name, character_hero):
        try:
            # TODO login to DB
            if True:
                self.character_name = character_name
                self.character_hero = character_hero
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def character_list(self):
        try:
            return_string = "Fetching data from DB\n1\n2\n3"
            return return_string
        except Exception as e:
            print(e)
            return False
        
    def dungeon_size_set(self, dungeon_size):
        if not dungeon_size == 1 and 2 and 3:
            return False
        if dungeon_size == "Small":
            self.dungeon_size = 4
        elif dungeon_size == "Medium":
            self.dungeon_size = 5
        else:
            self.dungeon_size = 6
        return True

    def dungeon_corner(self, dungeon_corner):
        if not dungeon_corner == 1 and 2 and 3 and 4:
            return False
        if dungeon_corner == 1:
            self.dungeon_corner = "North West"
        if dungeon_corner == 2:
            self.dungeon_corner = "North East"
        if dungeon_corner == 3:
            self.dungeon_corner = "South West"
        else:
            self.dungeon_corner = "South East"
        return True
