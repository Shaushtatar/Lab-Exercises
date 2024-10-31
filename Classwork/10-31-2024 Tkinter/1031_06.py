import tkinter as tk

root = tk.Tk()
root.title("Dropdown practice")
root.geometry("400x400") 

item_list = ["Yellow", "Blue", "Green", "Purple", "Violet"]

def chosen_option():
    color = value.get()
    root.configure(background=color)
    
    result_label = tk.Label(root, text=f"You chose {color}!")
    result_label.pack()
    
    value.set("Select a color")
    
    return color

#set() est's the initial value
value = tk.StringVar()
value.set("Select a color")

#dropdownmenu syntax, tie it to a tkinter variable and a list
dropdown = tk.OptionMenu(root, value, *item_list)
choose_btn = tk.Button(root, text="Click to choose", command=chosen_option)

dropdown.pack()
choose_btn.pack()

root.mainloop()
