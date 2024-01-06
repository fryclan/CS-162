"""
class to hold all gui stuff (hopfully)
"""

import tkinter as tk
import player_character
import random_rolls_class
import Spells

me = player_character.Adventurer()

# def Close():
#     player_character.root.destroy()
    
# class make_adventurer():
#     character_loop = ""
#     def set_character_loop(string):
#         character_loop = string
#         if character_loop == "N":
#             player_character.root.destroy()
#             exit
#             return 0 #close window end program
#         elif character_loop == "Y":
#             player_character.root.destroy()
#             return 1 #close window move to next window with other buttons
    
#     # label_1 = tk.Label(player_character.root, {"Do you want to Create a character", 1})
#     # label_1.pack()
       
#     yes_buton = tk.Button(player_character.root, text="Yes", 
#                         command=lambda: make_adventurer.set_character_loop("Y"))
#     yes_buton.pack()
    
#     no_buton = tk.Button(player_character.root, text="No", 
#                         command=lambda: make_adventurer.set_character_loop("N"))
#     no_buton.pack()
    
# x = make_adventurer()
# player_character.root.mainloop()

# me = player_character.Adventurer()


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

update_name_button = tk.Button(player_character.root, text="Update Stuff",
                   command=lambda: set_text(me.name, me.entry_stringvar.get()))
update_name_button.pack()

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

x = 0
y = 200
a = 0
    
# for i in Spells.wizard_cantrips:
#     a = a+1
#     spell_button = tk.Button(player_character.root, text=f"{i}",width= 25)
#     spell_button.place(x= x,y= y)
#     x = x+185
#     if(a%5 == 0):
#         y = y+30
#         x = 0
        
# a = 0
# y = y+60
# x = 0

# for i in Spells.wizard_level1:
#     a = a+1
#     spell_button = tk.Button(player_character.root, text=f"{i}",width= 25,)
#     spell_button.place(x= x,y= y)
#     x = x+185
#     if(a%5 == 0):
#         y = y+30
#         x = 0
        
# a = 0
# y = y+60
# x = 0   

# for i in Spells.cleric_cantrips:
#     a = a+1
#     spell_button = tk.Button(player_character.root, text=f"{i}",width= 25)
#     spell_button.place(x= x,y= y)
#     x = x+185
#     if(a%5 == 0):
#         y = y+30
#         x = 0
        
# a = 0
# y = y+60
# x = 0  

# for i in Spells.cleric_level1:
#     a = a+1
#     spell_button = tk.Button(player_character.root, text=f"{i}",width= 25)
#     spell_button.place(x= x,y= y)
#     x = x+185
#     if(a%5 == 0):
#         y = y+30
#         x = 0
        
# a = 0
# y = y+60
# x = 0  

def stat_boxes():
    x = 0
    y = 200
    for name in me._stats_list:
        int_var = tk.StringVar(player_character.root, random_rolls_class.roll_points())
        
        player_label = tk.Label(player_character.root,text= f"{name}")
        player_label.place(x= x,y= y)
        
        player_stat_box = tk.Entry(player_character.root, textvariable=int_var)
        player_stat_box.place(x= x,y= y+30)
        
        x = x+150
        
        player_character.root.update()

stat_button = tk.Button(player_character.root, text="Stat rolls",
                        command=lambda: stat_boxes())
stat_button.pack()

player_character.root.mainloop()
