#ChatGPT built this for me, I'm not about to figure out all of these --Prof. Gibson
#x, y coordinates 

import tkinter as tk

def draw_jack_o_lantern():
    # Create the main window
    root = tk.Tk()
    root.title("Jack-o'-Lantern")

    # Set up the canvas
    canvas = tk.Canvas(root, width=300, height=300, bg="black")
    canvas.pack()

    # Pumpkin base
    canvas.create_oval(50, 50, 250, 250, fill="OrangeRed3", outline="OrangeRed3")

    # Left eye
    canvas.create_polygon(100, 100, 120, 70, 140, 100, fill="black")

    # Right eye
    canvas.create_polygon(160, 100, 180, 70, 200, 100, fill="black")

    # Nose
    canvas.create_polygon(140, 140, 160, 140, 150, 170, fill="black")
    
    mouth_points = [
            (110, 190), (120, 190), (130, 200), (140, 190), 
            (150, 200), (160, 190), (170, 200), (180, 190),
            (190, 200), (200, 190), (190, 210), (180, 200),
            (170, 210), (160, 200), (150, 210), (140, 200),
            (130, 210), (120, 200), (110, 190)
        ]
    canvas.create_polygon(mouth_points, fill="black")

    root.mainloop()

draw_jack_o_lantern()


