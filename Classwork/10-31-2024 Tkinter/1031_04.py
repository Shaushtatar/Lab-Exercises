import tkinter as tk
def close_window():
    root.destroy()
def click():
    label = tk.Label(root, text = "Hooray!!!", fg="SpringGreen2")
    label.grid(row = 3, column = 0)
    
root = tk.Tk()
root.geometry("200x200")

button = tk.Button(root, text = "Click me!", command = click)
button.grid(row=0, column=0) #If you click it, you destroy the root (the window closes)

exit_button = tk.Button(root, text = "Exit", command = close_window)
exit_button.grid(row=0, column=3)

root.mainloop()