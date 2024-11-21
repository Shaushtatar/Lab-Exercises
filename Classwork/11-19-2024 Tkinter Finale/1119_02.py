from tkinter import *
import tkinter as tk
#inspired by https://www.youtube.com/watch?v=rG1SgFOzMqw

root = tk.Tk()
root.geometry("450x350")


#establish three different frames
main_frame = tk.Frame(root)
home_window = tk.Frame(main_frame,
                    pady=10, padx=10, background="black")
different_window = tk.Frame(main_frame,
                    pady=10, padx=10, background="yellow")

welcome_label = tk.Label(root, text="Welcome to this Application", 
                         font=("Times", 15, "italic"), pady=20)
welcome_label.pack()

main_frame.pack()
home_window.pack()

label_one = tk.Label(home_window, text="I am the home window",
                    font=("Garamond", 25))
label_two = tk.Label(different_window, text="I am a different window",
                    font=("Comic Sans", 25))

label_one.pack()
#pack label_two but the frame it's in isn't visible so it's not visible
label_two.pack()

#two functions to switch between the windows
#I forget one frame and one button, and raise one frame and one button
def change_window():
    home_window.forget()
    switch_button.forget()
    
    different_window.tkraise()
    return_button.tkraise()
    different_window.pack()
    return_button.pack(side=tk.BOTTOM, pady=10)
    
def return_home():
    different_window.forget()
    return_button.forget()
    
    home_window.tkraise()
    switch_button.tkraise()
    home_window.pack()
    switch_button.pack(side=tk.BOTTOM, pady=10)
    
#establish both buttons, only pack one to begin with     
switch_button = tk.Button(root, text="Go to new page", command=change_window)
return_button = tk.Button(root, text="Return to home", command=return_home)

#packing on the bottom
switch_button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
