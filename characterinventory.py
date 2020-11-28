
# this class' purpose is to help in making
# the character_inventory list that is in
# the FallOut44.py file/program
class CharacterInventory:
    def __init__(self, character_inventory):
        self.__character_inventory = character_inventory

    def set_character_inventory(self, character_inventory):
        self.__character_inventory = character_inventory

    def get_character_inventory(self):
        return self.__character_inventory

    def __str__(self):
        return self.__character_inventory
