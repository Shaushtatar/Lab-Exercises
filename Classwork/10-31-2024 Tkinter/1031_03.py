#Trying some tkinter

import tkinter as tk
#https://tkdocs.com/shipman/label.html
#https://tkdocs.com/shipman/fonts.html 
root = tk.Tk()
root.geometry("200x200")
label1 = tk.Label(root, text="Hello World!", background="lemon chiffon")
label2 = tk.Label(root, text="Goodbye World!", background="DarkOrchid2", foreground = "medium spring green")

label1.grid(row=0, column=0)
label2.grid(row=1, column=1)


button = tk.Button(root, text="BUTTON")
print(button.configure().keys())

root.mainloop()