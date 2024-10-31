#This is a very basic Tkinter window

#import syntax convention
import tkinter as tk

#creates the window, always known as "root"
root = tk.Tk()
#sets the window size
root.geometry("200x100") 

#creates a label (text) on the window
myLabel = tk.Label(root, text="Hello World!")
#Label can be thought of as a child class of our tkinter object
#places it on screen
myLabel.pack()
#We can also use .grid, but we can't use both pack and grid

#myLabel.grid(row=0, column=0)

#runs the event loop
root.mainloop()
