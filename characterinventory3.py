
# this class' purpose is to help in making
# the character_inventory3 list that is in
# the FallOut44.py file/program
class CharacterInventory3:
    def __init__(self, character_inventory3):
        self.__character_inventory3 = character_inventory3

    def set_character_inventory3(self, character_inventory3):
        self.__character_inventory3 = character_inventory3

    def get_character_inventory3(self):
        return self.__character_inventory3

    def __str__(self):
        return self.__character_inventory3
