"""
class to hold all gui stuff (hopfully)
"""

import tkinter as tk
import player_character
import random_rolls_class

me = player_character.Adventurer()

class make_adventurer():
    character_loop = ""
    def set_character_loop(string):
        character_loop = string
        if character_loop == "N":
            return 0 #close window end program
        elif character_loop == "Y":
            return 1 #close window move to next window with other buttons
        
    # yes_buton = tk.Button(player_character.root, text="Yes", 
    #                     command=lambda: set_character_loop("Y"))
    # yes_buton.pack()
    # no_buton = tk.Button(player_character.root, text="No", 
    #                     command=lambda: set_character_loop("N"))
    # no_buton.pack()
    # player_character.root.mainloop()


# def set_character_loop(string):
#     character_loop = string

# def stat_boxes():
#     int_var = tk.StringVar(player_character.root, random_rolls_class.roll_points())
#     for name in me._stats_list:
#         player_label = tk.Label(player_character.root, name)
#         player_label.pack()
#         player_stat_box = tk.Entry(player_character.root, textvariable=int_var)
#         player_stat_box.pack()
    
def set_text(entry_box,text):
    entry_box.delete(0,tk.END)
    entry_box.insert(0,text)
    return
def save_character():
    try:
            open(f"{me.name.get()}.txt", "x")
    except FileExistsError:
            open(f"{me.name.get()}.txt", "w")

        # opens with 
    f = open(f"{me.name.get()}.txt", "a")
        
    f.write(me.__str__())

button = tk.Button(player_character.root, text="Update Stuff",
                   command=lambda: set_text(me.name, me.entry_stringvar.get()))
button.pack()

# yes_buton = tk.Button(player_character.root, text="Yes", 
#                       command=lambda: set_character_loop("Y"))
# yes_buton.pack()
# no_buton = tk.Button(player_character.root, text="No", 
#                       command=lambda: set_character_loop("N"))
# no_buton.pack()

barbarian_button = tk.Button(player_character.root, text="Barbarian",
                             command=lambda: me.player_class(1))
barbarian_button.pack()
wizard_button = tk.Button(player_character.root, text="wizard",
                             command=lambda: me.player_class(2))
wizard_button.pack()
cleric_button = tk.Button(player_character.root, text="cleric",
                             command=lambda: me.player_class(3))
cleric_button.pack()

save_button = tk.Button(player_character.root, text="Save Character",
                        command=lambda: save_character())
save_button.pack()

# stat_button = tk.Button(player_character.root, text="Stat rolls",
#                         command=lambda: stat_boxes())
# stat_button.pack()

player_character.root.mainloop()
