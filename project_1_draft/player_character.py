"""class containing player character info"""

#imports the classes from other file
from adventure_classes import Barbarian, Wizard, Cleric
from random_rolls_class import roll_points
import tkinter as tk

root = tk.Tk()

class Adventurer:
    """class for creating an adventurer"""

    _stats_list = ["Strength", "Dexterity", "Constitution", "Wisdom", "Inteligence", "Charisma"]
    _skills_strength = ["Athletics"]
    _skills_dexterity = ["Acrobatics", "Sleight of Hand", "Stealth"]
    _skills_intelligence = ["Arcana", "History", "Investigation", "Nature", "Religion"]
    _skills_wisdom = ["Animal Handling", "Insight", "Medicine", "Perception", "Survival"]
    _skills_charisma = ["Deception", "Intimidation", "Performance", "Persuasion"]

    def __init__(self):
        self._inventory: dict = {}    
        self.level = 1
        self.name = str(input("what is your name: "))
        # self.entry_stringvar = tk.StringVar(root, "enter your name")
        # self.name = tk.Entry(root, textvariable=self.entry_stringvar)
        # self.entry_stringvar.set("Enter Your Name")
        # self.name.pack()
        self.stat_dict = {name: roll_points() for name in self._stats_list} #name: roll_points() for name in self._stats_list
        self.health:int = 0
        self.player_type = 0
        self.spells = []
        self.player_class()
        self.modifier_dict = {}
        self.Stat_modifier()
        self.skills_dict = {}
        self.Skills()
        self.new_character = (f"Your name is\n{self.name}\n\
Your class is\n{self.player_type}\nYour stats are\n\
{self.stat_dict}\nYour stat modifiers are\n\
{self.modifier_dict}\nYour skills are\n{self.skills_dict}\n\
You also know these spells\n{self.spells}\n\
These are the items in you inventory\n{self._inventory}")
   
    def add_to_inventory(self, item, quantity):
        """Add item to the inventory."""
        if item in self._inventory:
            self._inventory[item] += quantity
        else:
            self._inventory[item] = quantity
    
    def remove_from_inventory(self, item, quantity):
        """Remove item to the inventory."""
        if item in self._inventory:
            if quantity >= self._inventory[item]:
                del self._inventory[item]
            else:
                self._inventory[item] -= quantity
        else:
            print("Item is not in your Inventory.")
    
    def view_inventory(self):
        """Display the items in the Inventory."""
        print(self._inventory)

    def Stat_modifier(self):
        """does the math so you can have your stat modifiers.
        """
        for item in self.stat_dict:
            modifier = round((self.stat_dict[item] - 10) / 2)
            self.modifier_dict[item] = modifier

    def player_class(self):
        """loops through untill the user inputs an int that will match
          a class, then sets up the class with what it needs.
        """
        while self.player_type != (1 , 2 , 3 , 0):
            if self.player_type == 1:
                self.player_type = "Barbarian"
                player = Barbarian()
                self._inventory.update(Barbarian._starting_gear)
                break
            elif self.player_type == 2:
                self.player_type = "Wizard"
                player = Wizard()
                self.spells.append(player.magic())
                self._inventory.update(Wizard._starting_gear)
                break
            elif self.player_type == 3:
                self.player_type = "Cleric"
                player = Cleric()
                self.spells.append(player.magic())
                self._inventory.update(Cleric._starting_gear)
                break
            elif self.player_type == 0:
                try:
                    self.player_type = int(input("What class of adventurer do you want to be:\n1.) Barbarian 2.) Wizard 3.) Cleric\n"))
                except ValueError:
                    print(f"Not a valid option. Try a number\n")
                    self.player_type = int(input("What class of adventurer do you want to be:\n1.) Barbarian 2.) Wizard 3.) Cleric\n"))
            else:
                try:
                    print(f"{self.player_type} is not a valid option")
                    self.player_type = int(input("What class of adventurer do you want to be:\n1.) Barbarian 2.) Wizard 3.) Cleric\n"))
                except ValueError:
                    print(f"{self.player_type} is not a valid option. Try a number\n")
                    self.player_type = int(input("What class of adventurer do you want to be:\n1.) Barbarian 2.) Wizard 3.) Cleric\n"))

    def Skills(self):
        """takes the info from the stat modifiers to make your skills
        """
        for item in self._skills_strength:
            self.skills_dict[item] = self.modifier_dict["Strength"]
        for item in self._skills_dexterity:
            self.skills_dict[item] = self.modifier_dict["Dexterity"]
        for item in self._skills_intelligence:
            self.skills_dict[item] = self.modifier_dict["Inteligence"]
        for item in self._skills_wisdom:
            self.skills_dict[item] = self.modifier_dict["Wisdom"]
        for item in self._skills_charisma:
            self.skills_dict[item] = self.modifier_dict["Charisma"]

    def __str__(self) -> str:
        return self.new_character
    