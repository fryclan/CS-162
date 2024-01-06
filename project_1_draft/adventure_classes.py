"""class for an adventuring class that generates random stats and gives spell options."""

from numpy import random
import typing
import Spells
import logging
import player_character
from functools import partial
import tkinter as tk

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
        self.cantrips_avalible = self.known_cantrip
        self.level1_avalible = self.known_level1
        self.stupid_button_monkey = 0
        
    
    def cantrip_button_effects(self, str):
        """append self._cantrip with name of button pressed
        """
        cantrips_left = len(self._cantrip)
        if cantrips_left < self.known_cantrip:
            self._cantrip.append(str)
            self.cantrips_avalible = self.cantrips_avalible - 1
            cantrip_left_label = tk.Label(player_character.root, text=f"Cantrips Avalible: {self.cantrips_avalible}")
            cantrip_left_label.place(x=450, y=286)
            player_character.root.update()
        else:
            cantrip_label = tk.Label(player_character.root, text=f"no more cantrips {self.stupid_button_monkey}")
            cantrip_label.place(x=500, y=806)
            player_character.root.update()
            self.stupid_button_monkey=self.stupid_button_monkey-1
        
    def level1_button_effects(self, str):
        """append self._Level1 with name of button pressed
        """
        level1_left = len(self._level1)
        if level1_left < self.known_level1:
            self._level1.append(str)
            self.level1_avalible = self.level1_avalible - 1
            level1_left_label = tk.Label(player_character.root, text=f"Level 1 Spells Avalible: {self.level1_avalible}")
            level1_left_label.place(x=450, y= 531)
            player_character.root.update()
        else:
            level1_label = tk.Label(player_character.root, text=f"no more spells {self.stupid_button_monkey}")
            level1_label.place(x=380, y=806)
            player_character.root.update()
            self.stupid_button_monkey=self.stupid_button_monkey-1
            
    def save_spells(self):
        self._cantrip.append(self._level1)

    def magic(self):
        """Function for setting up magic for an wizard.

        Returns:
            A list that is a combination of all the spells you chose.
        """ 
        
        x = 0
        y = 306
        a = 0
        cantrip_left_label = tk.Label(player_character.root, text=f"Cantrips Avalible: {self.cantrips_avalible}")
        cantrip_left_label.place(x=450, y=286)
        for cantrip in Spells.wizard_cantrips:
            
            spell_button = tk.Button(player_character.root, text=f"{cantrip}",width= 25, 
                                     command=partial(self.cantrip_button_effects, Spells.wizard_cantrips[a]))
            spell_button.place(x= x,y= y)
            a = a+1
            x = x+185
            if(a%5 == 0):
                y = y+30
                x = 0
            player_character.root.update()
        
        x = 0
        y = y+60
        a = 0
        level1_left_label = tk.Label(player_character.root, text=f"level1s Avalible: {self.level1_avalible}")
        level1_left_label.place(x=450, y= y-20)
        for level1 in Spells.wizard_level1:
                
            spell_button = tk.Button(player_character.root, text=f"{level1}",width= 25,
                                        command=partial(self.level1_button_effects, Spells.wizard_level1[a]))
            spell_button.place(x= x,y= y)
            a = a+1
            x = x+185
            if(a%5 == 0):
                y = y+30
                x = 0
            player_character.root.update()
        save_spells_button = tk.Button(player_character.root, text="Save Spells", 
                                       command=lambda: self.save_spells())
        save_spells_button.place(x= 450, y=836)

        return self._cantrip
        
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
        self.cantrips_avalible = self.known_cantrip
        self.level1_avalible = self.known_level1
        self.stupid_button_monkey = 0
        
    def cantrip_button_effects(self, str):
        """append self._cantrip with name of button pressed
        """
        cantrips_left = len(self._cantrip)
        if cantrips_left < self.known_cantrip:
            self._cantrip.append(str)
            self.cantrips_avalible = self.cantrips_avalible - 1
            cantrip_left_label = tk.Label(player_character.root, text=f"Cantrips Avalible: {self.cantrips_avalible}")
            cantrip_left_label.place(x=450, y=286)
            player_character.root.update()
        else:
            cantrip_label = tk.Label(player_character.root, text=f"no more cantrips {self.stupid_button_monkey}")
            cantrip_label.place(x=500, y=806)
            player_character.root.update()
            self.stupid_button_monkey=self.stupid_button_monkey-1
            
    def level1_button_effects(self, str):
        """append self._Level1 with name of button pressed
        """
        level1_left = len(self._level1)
        if level1_left < self.known_level1:
            self._level1.append(str)
            self.level1_avalible = self.level1_avalible - 1
            level1_left_label = tk.Label(player_character.root, text=f"Level 1 Spells Avalible: {self.level1_avalible}")
            level1_left_label.place(x=450, y= 370)
            player_character.root.update()
        else:
            level1_label = tk.Label(player_character.root, text=f"no more spells {self.stupid_button_monkey}")
            level1_label.place(x=380, y=806)
            player_character.root.update()
            self.stupid_button_monkey=self.stupid_button_monkey-1
            
    def save_spells(self):
        self._cantrip.append(self._level1)
        
    def magic(self):
        """Function for setting up magic for an cleric.

        Returns:
            A list that is a combination of all the spells you chose.
        """
        x = 0
        y = 306
        a = 0
        
        cantrip_left_label = tk.Label(player_character.root, text=f"Cantrips Avalible: {self.cantrips_avalible}")
        cantrip_left_label.place(x=450, y=286)
        
        for cantrip in Spells.cleric_cantrips:
            
            spell_button = tk.Button(player_character.root, text=f"{cantrip}",width= 25, 
                                     command=partial(self.cantrip_button_effects, Spells.cleric_cantrips[a]))
            spell_button.place(x= x,y= y)
            a = a+1
            x = x+185
            if(a%5 == 0):
                y = y+30
                x = 0
            player_character.root.update()
        
        x = 0
        y = y+60
        a = 0
        
        level1_left_label = tk.Label(player_character.root, text=f"level1s Avalible: {self.level1_avalible}")
        level1_left_label.place(x=450, y= y-20)
        
        for level1 in Spells.cleric_level1:
                
            spell_button = tk.Button(player_character.root, text=f"{level1}",width= 25,
                                        command=partial(self.level1_button_effects, Spells.cleric_level1[a]))
            spell_button.place(x= x,y= y)
            a = a+1
            x = x+185
            if(a%5 == 0):
                y = y+30
                x = 0
            player_character.root.update()

        save_spells_button = tk.Button(player_character.root, text="Save Spells", 
                                       command=lambda: self.save_spells())
        save_spells_button.place(x= 450, y=836)

        return self._cantrip
