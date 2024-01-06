"""class containing player character info"""

#imports the classes from other file
from adventure_classes import Barbarian, Wizard, Cleric
from random_rolls_class import roll_points
import tkinter as tk

root = tk.Tk()
root.geometry("926x943")

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
        # self.name = str(input("what is your name: "))
        self.entry_stringvar = tk.StringVar(root, "enter your name")
        self.name = tk.Entry(root, textvariable=self.entry_stringvar)
        self.name.pack()
        # self.stat_boxes()
        self.stat_dict = {name: roll_points() for name in self._stats_list} #name: roll_points() for name in self._stats_list
        # self.stat_value = [name: roll_points() for name in self._stats_list]
        # self.entry_stat_boxes = tk.StringVar(root, f"{self.stat_dict}")
        # self.stat_boxes = tk.Entry(root, textvariable=self.entry_stat_boxes)#(name: tk.Entry(root, textvariable=self.stat_dict) for name in self._stats_list)
        # self.stat_boxes.pack()
        self.health:int = 0
        self.player_type = ""
        self.spells = []
        self.modifier_dict = {}
        self.Stat_modifier()
        self.skills_dict = {}
        self.Skills()
#         self.new_character = (f"Your name is\n{self.name.get}\n\
# Your class is\n{self.player_type}\nYour stats are\n\
# {self.stat_dict}\nYour stat modifiers are\n\
# {self.modifier_dict}\nYour skills are\n{self.skills_dict}\n\
# You also know these spells\n{self.spells}\n\
# These are the items in you inventory\n{self._inventory}")

    # def stat_boxes(self):
    #     int_var = tk.IntVar(root, roll_points())
    #     for name in self._stats_list:
    #         player_label = tk.Label(root, name)
    #         player_label.pack()
    #         player_stat_box = tk.Entry(root, textvariable=int_var)
    #         player_stat_box.pack()

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
            stat_value = self.stat_dict[item]
            modifier = (self.stat_dict[item] - 10) // 2
            self.modifier_dict[item] = modifier

    def player_class(self, txt=0):
        """loops through untill the user inputs an int that will match
          a class, then sets up the class with what it needs.
        """
        while txt != (1 , 2 , 3 , 0):
            if txt == 1:
                self.player_type = "Barbarian"
                player = Barbarian()
                self._inventory.update(Barbarian._starting_gear)
                break
            elif txt == 2:
                self.player_type = "Wizard"
                player = Wizard()
                self.spells.append(player.magic())
                self._inventory.update(Wizard._starting_gear)
                break
            elif txt == 3:
                self.player_type = "Cleric"
                player = Cleric()
                self.spells.append(player.magic())
                self._inventory.update(Cleric._starting_gear)
                break
            # elif txt == 0:
            #     try:
            #         txt = int(input("What class of adventurer do you want to be:\n1.) Barbarian 2.) Wizard 3.) Cleric\n"))
            #     except ValueError:
            #         print(f"Not a valid option. Try a number\n")
            #         txt = int(input("What class of adventurer do you want to be:\n1.) Barbarian 2.) Wizard 3.) Cleric\n"))
            # else:
            #     try:
            #         print(f"{txt} is not a valid option")
            #         txt = int(input("What class of adventurer do you want to be:\n1.) Barbarian 2.) Wizard 3.) Cleric\n"))
            #     except ValueError:
            #         print(f"{txt} is not a valid option. Try a number\n")
            #         txt = int(input("What class of adventurer do you want to be:\n1.) Barbarian 2.) Wizard 3.) Cleric\n"))

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
        return (f"Your name is\n{self.name.get()}\n\
Your class is\n{self.player_type}\nYour stats are\n\
{self.stat_dict}\nYour stat modifiers are\n\
{self.modifier_dict}\nYour skills are\n{self.skills_dict}\n\
You also know these spells\n{self.spells}\n\
These are the items in you inventory\n{self._inventory}")
    