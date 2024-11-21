#adapted from
#https://pythonassets.com/posts/hyperlink-button-in-tk-tkinter/
import tkinter as tk
from tkinter.font import Font
import webbrowser


class Linkbutton(tk.Button):

    #https://realpython.com/python-kwargs-and-args/
    '''args stands for “non-keyword” or “positional” arguments, aka mandatory parameters. 
    When we add our wildcard * symbol in front of it, it tells our Child class to inherit 
    all of the mandatory arguments from the Parent class
    '''

    '''Similarly, kwargs stands for “keyword arguments” aka optional parameters 
    the ** tells Python to look for keyword arguments (aka key=value)
    It also passes any of those from the Parent into the Child class
    '''

    def __init__(self, *args, **kwargs): #star means "all" -- so all arguments
        super().__init__(*args, **kwargs) #double-star ** 
        self.configure(foreground="#357fde", font=("Arial", 20))
        self["cursor"] = "hand2"
        self.bind("<Enter>", self.on_mouse_enter)
        self.bind("<Leave>", self.on_mouse_leave)

    def on_mouse_enter(self, event):
        self.configure(font =("Arial", 20, "underline"))

    def on_mouse_leave(self, event):
        self.configure(font =("Arial", 20))


root = tk.Tk()
root.title("Hyperlink in Tk")
root.geometry("400x300")
linkbutton = Linkbutton(
    text="google.com",
    command=lambda: webbrowser.open("https://google.com")
)
linkbutton.place(x=50, y=50)
root.mainloop()


