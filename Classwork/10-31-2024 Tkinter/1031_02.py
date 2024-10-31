#visualizing the grid
import random
import tkinter as tk

root = tk.Tk()
root.geometry("833x833")

colors = ["red", "green", "blue",
         "orange", "yellow", "purple"]

for x in range(7):
    for y in range(8):
        tk.Label(root, text=None, background=random.choice(colors),
             borderwidth=2, padx=50, pady=50,
             relief="solid").grid(row=x, column=y)

root.mainloop() 


