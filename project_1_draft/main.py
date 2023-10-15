
import player_character
import tkinter as tk

character_loop = ""

while character_loop != "N":
    character_loop = input("Do you want to make an adventurer: Y/N\n").strip().title()
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

label = tk.Label(player_character.root, text=me.new_character)
label.pack()
player_character.root.mainloop()

    