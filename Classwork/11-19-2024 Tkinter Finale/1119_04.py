import tkinter as tk

root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")
root.configure(background="dark green")

#there's no way to globally style the font color unfortunately
#You still have to set the "foreground" parameter for each widget
root.option_add("*Font", "Arial 12") #all instances, indicated by the *
root.option_add("*Label.Background", "dark green") 
root.option_add("*Frame.Background", "dark green")
root.option_add("*Button.Background", "dark sea green")
root.option_add("*Button.Foreground", "white")
root.option_add("*Button.Padding", 5)


#establish three different frames
main_frame = tk.Frame(root)
home_window = tk.Frame(main_frame,
                    pady=30, padx=10)
different_window = tk.Frame(main_frame,
                    pady=30, padx=10)

welcome_label = tk.Label(root, text="Welcome to this Application", 
                         pady=20, foreground="white")
welcome_label.pack()

main_frame.pack()
home_window.pack()

label_one = tk.Label(home_window, text="I am the home window", foreground="white")
label_two = tk.Label(different_window, text="I am a different window", foreground="white")

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
