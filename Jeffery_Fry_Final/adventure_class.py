"""class for an adventuring class that generates random stats and gives spell options."""

from numpy import random
import typing
import Spells
import logging
import re #This is the regex library really helpful to lear regex....!@!@@@@

#TODO Learn Regex

logging.basicConfig(filename = f'./Logs/{__name__}.log', 
                    level=logging.DEBUG, 
                    format='%(filename)s:%(lineno)s %(levelname)s:%(message)s')


def roll_points():
    """Creates a number to use as a stat following the requirements 
    for a 5e dnd character

    Returns:
        A int
    """
    points = [random.randint(1, 6) for _ in range(4)]
    lowest = min(points)
    points.remove(lowest)
    return sum(points)

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

        while self.known_cantrip > 0:
            # phone_number = re.compile(r'(\d{3}) \d{3}-\d{4}')
            print(f"you are allowed to learn {self.known_cantrip} cantrips.")
            spell = input(f"what spell would you like to learn:\n{Spells.wizard_cantrips}\n").strip().title()
            logging.debug(spell)
            # logging.debug(phone_number.findall(spell))

            if spell in self._cantrip:
                print("you already know that spell.\n")
                
            elif spell not in Spells.wizard_cantrips:
                print(f"you arn't allowed to learn {spell} please pick from the list.\n")

            else:
                self._cantrip.append(spell)
                self.known_cantrip -= 1
             
        while self.known_level1 > 0:
            print(f"you are allowed to learn {self.known_level1} level 1 spells.\n")
            spell = input(f"what spell would you like to learn:\n{Spells.wizard_level1}\n").strip().title()
                
            if spell in self._level1:
                print("you already know that spell.\n")

            elif spell not in Spells.wizard_level1:
                print(f"you arn't allowed to learn {spell} please pick from the list.\n")
                
            else:
                self._level1.append(spell)
                self.known_level1 -= 1


            #This is how my brother would do it, I asked for help to fix somthing and he wanted to teach me stuff :).  


            # while len(self._cantrip) < self.known_cantrip:
            #     print("you are allowed to learn 3 cantrips.")
            #     spell = input(f"what spell would you like to learn:\n{Spells.wizard_cantrips}")
            #     self._cantrip.append(spell) if spell not in self._cantrip else print("you already know that spell.")

            # while len(self._level1) < self.known_level:
            #     print("you are allowed to learn 3 cantrips.")
            #     spell = input(f"what spell would you like to learn:\n{Spells.wizard_level1}")
            #     self._level1.append(spell) if spell not in self._level1 else print("you already know that spell.")



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
        while self.known_cantrip > 0:
            print(f"you are allowed to learn {self.known_cantrip} cantrips.")
            #spell = str.title(input(f"what spell would you like to learn:\n{Spells.cleric_cantrips}\n"))
            spell = input(f"what spell would you like to learn:\n{Spells.cleric_cantrips}\n").strip().title()
            
            if spell in self._cantrip:
                print("you already know that spell.\n")
                
            elif spell not in Spells.cleric_cantrips:
                print(f"you arn't allowed to learn {spell} please pick from the list.\n")

            else:
                self._cantrip.append(spell)
                self.known_cantrip -= 1
             
        while self.known_level1 > 0:
            print(f"you are allowed to learn {self.known_level1} level 1 spells.\n")
            spell = str.title(input(f"what spell would you like to learn:\n{Spells.cleric_level1}\n"))
                
            if spell in self._level1:
                print("you already know that spell.\n")

            elif spell not in Spells.cleric_level1:
                print(f"you arn't allowed to learn {spell} please pick from the list.\n")
                
            else:
                self._level1.append(spell)
                self.known_level1 -= 1
        return self._cantrip + self._level1
