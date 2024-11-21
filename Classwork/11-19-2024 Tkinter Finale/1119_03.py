import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")
root.configure(background="white")


def open_new_window():
    
    # Create a Toplevel window
    new_window = tk.Toplevel(root)
    new_window.title("Secondary Window")
    new_window.geometry("300x200")
    new_window.configure(background="purple")

    label = tk.Label(new_window, text="This is a secondary window!", font=("Arial", 14))
    entry = tk.Entry(new_window)
    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    
    label.pack(pady=10)
    entry.pack(pady=5)
    close_button.pack(pady=10)

    def on_close():
        msg = messagebox.askokcancel("Close", "Do you really want to close this window?")
        if msg: 
            new_window.destroy()
            
    #this allows us to override what happens when someone presses the "x"
    #for the window, it double checks if they want to close it
    new_window.protocol("WM_DELETE_WINDOW", on_close)
    
main_label = tk.Label(root, text="Welcome to the Main Window!", font=("Arial", 16))
open_button = tk.Button(root, text="Open New Window", command=open_new_window)

main_label.pack(pady=20)
open_button.pack(pady=10)


root.mainloop()
