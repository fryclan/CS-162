
import player_character
import tkinter as tk
# import gui_class

character_loop = ""

def set_character_loop(string):
    character_loop = string
    
def set_text(entry_box,text):
    entry_box.delete(0,tk.END)
    entry_box.insert(0,text)
    return

button = tk.Button(player_character.root, text="Update Stuff",
                   command=lambda: set_text(me.name, me.entry_stringvar.get()))
button.pack()
yes_buton = tk.Button(player_character.root, text="Yes", 
                      command=lambda: set_character_loop("Y"))
yes_buton.pack()
No_buton = tk.Button(player_character.root, text="No", 
                      command=lambda: set_character_loop("N"))
No_buton.pack()

# def update_stuff():
#     """update info when button is pressed
#     """
#     if button:
#         me.entry_stringvar.set()
#         me.statbox.set()
        
# update_stuff()

# label = tk.Label(player_character.root, text=me.new_character)
# label.pack()
player_character.root.mainloop()

while character_loop != "N":
    # character_loop = input("Do you want to make an adventurer: Y/N\n").strip().title()
    if character_loop == "Y":
        if __name__ == "__main__":
            me = player_character.Adventurer()
            """sends all of the information to a file with the same name you gave
            your adventurer will overwrite any duplacates."""
        # Path
        try:
            open(f"{me.name}.txt", "x")
        except FileExistsError:
            open(f"{me.name}.txt", "w")

        # opens with 
        f = open(f"{me.name}.txt", "a")
        
        f.write(me.new_character)
        
        character_loop = input("do you want to make an adventurer: Y/N\n").strip().title()
        
        f.close
    elif character_loop == "N":
        print("Goodbye!")
        break
    
    else:
        print("Not a valid input try again")
        continue
