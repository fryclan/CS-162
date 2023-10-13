
import player_character




character_loop = input("do you want to make an adventurer: Y/N\n").strip().title()
while character_loop == "Y":
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
    
else: #character_loop != "Y"
    print("Goodbye!")
    