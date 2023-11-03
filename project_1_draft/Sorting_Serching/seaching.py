"""_summary_
"""
import tkinter as tk
import list_1_100

# root = tk.Tk()



# print(list_1_100.random_number_list)
user_int = int(input(f"please give me an int to search: "))
def search(list, term):
    """Definition for searching a list[]

    Args:
        list (_type_): list of info to be searched
        term (_type_): term to be searched

    Returns:
        _type_: position of item in list 
    """
    # print(f"string len in def {len(list)}")
    # print(f"term to be searched in def {term}")
    for i in range(len(list)):
        if list[i] == term:
            print(f"postion of found term: {i}")
            return True
    return False

# def set_text(entry_box,text):
#     entry_box.delete(0,tk.END)
#     entry_box.insert(0,text)
#     return


# intvar = tk.IntVar(root, value = 1)
# entry_box = tk.Entry(root, textvariable = intvar)
# entry_box.pack()

# position_stringVar = tk.StringVar(root, f"{q}")
# result_entry = tk.Entry(root, text=position_stringVar)
# button_2 = tk.Button(root, text= "position update", command=lambda: set_text(result_entry, position_stringVar.get()))
        
# button = tk.Button(root, text="Search",
#                    command=lambda: search(list_1_100.random_number_list, entry_box.get()))
# button.pack()
# # search_results = tk.Label(root, text=list_1_100.random_number_list)
# # search_results.pack()
# result_entry.pack()
# button_2.pack()

if search(list_1_100.random_number_list, user_int):
    print(f"found {user_int}")
else:
    print(f"didnt find {user_int}")

# root.mainloop()
        