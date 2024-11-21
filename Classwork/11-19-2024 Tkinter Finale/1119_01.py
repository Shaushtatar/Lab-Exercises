#Canvases are the way to show graphics on Tkinter
import tkinter as tk
from PIL import ImageTk, Image
root = tk.Tk()
root.geometry("800x400")
canvas = tk.Canvas(root)
def display():
    path = r"C:\Users\billy\Downloads\Pork.webp"
    image = Image.open(path)
    photo = ImageTk.PhotoImage(image, master = root)
    canvas.create_image(100,100, anchor = "center", image=photo)
    canvas.image = photo
    canvas.pack()
    text_widget.pack(side="left", fill="both", expand=True)

    
button = tk.Button(root, text="Press for Armenian Cory", command = display, pady = 10)
button.pack()

text_widget = tk.Text(root, wrap="word",
                      height = 10, width = 10,
                      font=("Garamond", 56))

scrollbar = tk.Scrollbar(root, orient="vertical", 
                         command=text_widget.yview)

#linking text to scrollbar, its for the y-axis only
text_widget.config(yscrollcommand=scrollbar.set)

sample_text = "I am the sample text attatched to this scrollable window"
text_widget.insert("1.0", sample_text)

#expand = True has the text widget fill the screen as you adjust window size
text_widget.pack(side="left", fill="both", expand=True)
#notice I'm putting the scrollbar on the right
#and having it fill the y axis
scrollbar.pack(side="right", fill="y")


root.mainloop()
