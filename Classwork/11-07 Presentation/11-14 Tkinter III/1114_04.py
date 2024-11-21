import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
#Frames are children of roots
#So everything in frames will be grandchildren of roots

b1frame = tk.Frame(root)
b2frame = tk.Frame(root)
b3frame = tk.Frame(root)
b4frame = tk.Frame(root)

button1 = tk.Button(b1frame, text = "I am a button")
button2 = tk.Button(b2frame, text = "I am also a button")
button3 = tk.Button(b3frame, text = "I am ALSO a button")
button4 = tk.Button(b4frame, text = "I span all the buttons")

b1frame.grid(row=0, column=0, pady=30)
b2frame.grid(row=0, column=1, pady=30)
b3frame.grid(row=0, column=2, pady=30)
b4frame.grid(row=1, columnspan=3, pady=10)

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()
