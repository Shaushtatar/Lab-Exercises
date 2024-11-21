import tkinter as tk
import webbrowser

root = tk.Tk()
root.geometry("750x250")

#Define a callback function
def callback(url):
    webbrowser.open_new_tab(url)

#Create a Label to display the link
link = tk.Label(root, text="Google",
             font=('Helveticabold', 15), fg="blue", 
             cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
callback("http://www.google.com"))

root.mainloop()
'''
 <KeyPress> or <KeyRelease>
Looks for keys pressed or released. Can look for a singular key, eg. <KeyPress-Escape> or <KeyRelease-Escape>
<Button-1> or <Button-Release-1>
Left mouse click or release 
<Button-2> or <Button-Release-2>
Right mouse click or release
<Motion>
Detecting any mouse movement on the screen
<Double-1>
Double click with left mouse button
<MouseWheel>
Detects the scrolling up and down of a mouse wheel, called <Button-4> for macs
<Enter> or <Leave>
When the mouse pointer enters or leaves the widget's area
'''