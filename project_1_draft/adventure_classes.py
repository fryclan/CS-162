"""class for an adventuring class that generates random stats and gives spell options."""

from numpy import random
import typing
import Spells
import logging
# import re #This is the regex library really helpful to lear regex....!@!@@@@

#TODO Learn Regex

# logging.basicConfig(filename = f'./Logs/{__name__}.log', 
#                     level=logging.DEBUG, 
#                     format='%(filename)s:%(lineno)s %(levelname)s:%(message)s')

class Barbarian:
    _starting_gear = {"Great Axe" : 1, 
                      "Hand Axe" : 2,
                      "Javelins" : 4,
                      "Explorers Pack" : 1}
    _hitdie = 12

class Wizard:
    _starting_gear = {"Dagger" : 1, 
                        "Arcane Focus" : 1,
                        "Explorers Pack" : 1,
                        "Spellbook" : 1}
    _hitdie = 4
    
    def __init__(self): 
        self._cantrip: typing.List[str] = []
        self._level1: typing.List[str] = []
        self.known_cantrip: int = 3
        self.known_level1: int = 2

    def magic(self):
        """Function for setting up magic for an wizard.

        Returns:
            A list that is a combination of all the spells you chose.
        """ 
        
        while len(self._cantrip) < self.known_cantrip:
            print("you are allowed to learn 3 cantrips.")
            spell = input(f"what spell would you like to learn:\n{Spells.wizard_cantrips}")
            self._cantrip.append(spell) if spell not in self._cantrip else print("you already know that spell.")

        while len(self._level1) < self.known_level1:
            print("you are allowed to learn 3 cantrips.")
            spell = input(f"what spell would you like to learn:\n{Spells.wizard_level1}")
            self._level1.append(spell) if spell not in self._level1 else print("you already know that spell.")



        return self._cantrip + self._level1
        
class Cleric:
    _starting_gear = {"Mace" : 1,
                      "Scale Mail" : 1,
                      "Light Crossbow" : 1,
                      "Bolts" : 20,
                      "Explorers Pack" : 1,
                      "Shield" : 1,
                      "Holy Symbol" : 1,}
    _hitdie = 8
    def __init__(self):
        
        self._cantrip: typing.List[str] = []
        self._level1: typing.List[str] = []
        self.known_cantrip: int = 3
        self.known_level1: int = 2
        
    def magic(self):
        """Function for setting up magic for an wizard.

        Returns:
            A list that is a combination of all the spells you chose.
        """
        while len(self._cantrip) < self.known_cantrip:
            print("you are allowed to learn 3 cantrips.")
            spell = input(f"what spell would you like to learn:\n{Spells.cleric_cantrips}")
            self._cantrip.append(spell) if spell not in self._cantrip else print("you already know that spell.")

        while len(self._level1) < self.known_level1:
            print("you are allowed to learn 3 cantrips.")
            spell = input(f"what spell would you like to learn:\n{Spells.cleric_level1}")
            self._level1.append(spell) if spell not in self._level1 else print("you already know that spell.")

        return self._cantrip + self._level1
        
