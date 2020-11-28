
# this class' purpose is to help in making
# the character_inventory2 list that is in
# the FallOut44.py file/program
class CharacterInventory2:
    def __init__(self, character_inventory2):
        self.__character_inventory2 = character_inventory2

    def set_character_inventory2(self, character_inventory2):
        self.__character_inventory2 = character_inventory2

    def get_character_inventory2(self):
        return self.__character_inventory2

    def __str__(self):
        return self.__character_inventory2
