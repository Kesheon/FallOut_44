
# this class' purpose is to help in making
# the character_inventory4 list that is in
# the FallOut44.py file/program
class CharacterInventory4:
    def __init__(self, character_inventory4):
        self.__character_inventory4 = character_inventory4

    def set_character_inventory4(self, character_inventory4):
        self.__character_inventory4 = character_inventory4

    def get_character_inventory4(self):
        return self.__character_inventory4

    def __str__(self):
        return self.__character_inventory4
