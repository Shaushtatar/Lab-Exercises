import tkinter as tk
root = tk.Tk()
root.geometry("200x200")
#getting data from user input and storing it
def get_data():
    username = user_entry.get()
    password = pass_entry.get()
    user_entry.delete(0, "end")
    pass_entry.delete(0,"end")
    print(username, password)

user_label = tk.Label(root, text="Username")
user_entry = tk.Entry(root, width=35, borderwidth=5) #input bars in our window are called entry
pass_label = tk.Label(root, text="Password")
pass_entry = tk.Entry(root, width=35, borderwidth=5)
button = tk.Button(root, text="Log-In", command=get_data)

user_entry.pack()
user_label.pack()
pass_entry.pack()
pass_label.pack()
button.pack()

root.mainloop()