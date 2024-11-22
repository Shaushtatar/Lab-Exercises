import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont
root = tk.Tk()
root.geometry("400x200")


def open_page(username, password):
    if username == "mcahill@facebook.com" and password == "hitchcock319":
        secondary = tk.Toplevel(root)
        secondary.geometry("890x686")
        secondary.configure(background="white")
        secondary.title("Facebook")
        def destroy(event):
            secondary.destroy()
        secondary.bind("<Escape>", destroy)
        #Helped with binding and event syntax https://python-course.eu/tkinter/events-and-binds-in-tkinter.php
        cal18bold = tkFont.Font(family = "Calibri", size = 18, weight = "bold")
        #Frames
        #===========================================================================================
        sideframe = tk.Frame(secondary, background = "white", width = 160, height = 686)
        mainframe = tk.Frame(secondary, background = "white", width = 730, height = 662, pady = 12)
        #https://www.youtube.com/watch?v=lH1y7kiDeyg
        #I used this tutorial to help me arrange frames next to each other while using pack
        sideframe.pack(side = "left")
        mainframe.pack(side = "right")
        #*******************************************************************************************
        header = tk.Frame(mainframe, background = "royalblue4", width = 730, height = 68)
        body = tk.Frame(mainframe, background = "pink", width = 730, height = 594)
        header.pack()
        body.pack()
        #*******************************************************************************************
        body_left = tk.Frame(body, background = "white", width = 260, height = 594)
        body_right = tk.Frame(body, background="red", width = 470, height = 594)
        body_left.pack(side = "left")
        body_right.pack(side = "right")
        #*******************************************************************************************
        imgbox = tk.Frame(body_left, background = "white", width = 260, height = 434)
        editbox = tk.Frame(body_left, background = "white", width = 260, height = 160)
        imgbox.pack()
        editbox.pack()
        #*******************************************************************************************
        contacts = tk.Frame(body_right, background="white", width = 470, height = 218)
        dropdowns = tk.Frame(body_right, background="white", width = 470, height = 376)
        contacts.pack()
        dropdowns.pack()
        #*******************************************************************************************
        sideframe_top = tk.Frame(sideframe, width = 160, height = 64, background = "white")
        sideframe_bottom = tk.Frame(sideframe, width = 160, height = 622, background = "white")
        sideframe_top.pack()
        sideframe_bottom.pack()
        #*******************************************************************************************
        header_top = tk.Frame(header, background = "royalblue4", width = 730, height = 40)
        header_bottom = tk.Frame(header, background = "royalblue2", width = 730, height = 28)
        header_top.pack()
        header_bottom.pack()
        #*******************************************************************************************
        logoframe = tk.Frame(header_top, width = 107, height = 40, background = "royalblue4")
        nonlogoframe = tk.Frame(header_top, width = 623, height = 40, background = "royalblue4")
        logoframe.pack(side = "left")
        nonlogoframe.pack(side = "right")
        #===========================================================================================
        canvas = tk.Canvas(imgbox, width = 260, height = 434, background = "white")
        canvas.pack()
        path = r"C:\Users\billy\OneDrive\Documents\GitHub\Lab-Exercises\Lab 10\matt.jpg"
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image) #went into MS paint to adjust the actual image size
        canvas.create_image(130, 217, anchor = "center", image=photo) #<260,434>/2 = <130,217> -- this is center of frame
        canvas.image = photo

        sideheader = tk.Canvas(sideframe_top, width = 160, height = 40, background = "white")
        sideheader.pack()
        path2 = r"C:\Users\billy\OneDrive\Documents\GitHub\Lab-Exercises\Lab 10\mysterious_guy.jpg"
        topimage = Image.open(path2)
        sideheaderphoto = ImageTk.PhotoImage(topimage)
        sideheader.create_image(80, 20, anchor = "center", image = sideheaderphoto)


        logo = tk.Canvas(logoframe, width = 105, height = 38, background = "royalblue4")
        logo.place(x=0, y=0)
        logopath = r"C:\Users\billy\OneDrive\Documents\GitHub\Lab-Exercises\Lab 10\facebooklogo.jpg"
        logoim = Image.open(logopath)
        logoto = ImageTk.PhotoImage(logoim)
        logo.create_image(54, 20, anchor = "center", image = logoto)

        barentries = tk.Label(nonlogoframe, text = "                      home  search   browse   share   invite   help", fg = "white", bg = "royalblue4")
        barentries.place(x=200, y=10)
        exitbutton = tk.Button(nonlogoframe, text = "logout", fg = "white", background = "royalblue4", command=secondary.destroy)
        exitbutton.place(x = 550, y = 10)
        #I don't really know why, but whenever I packed barentries and logo it broke the logo and nonlogo frames
        #and they wouldn't show up where they were supposed to. 
        #https://stackoverflow.com/questions/13111679/positioning-canvas-in-window-tkinter-python
        #I was recommended by this thread to just use place instead of pack for this frame, and it worked well
        space = "                                                          "
        profilename = tk.Label(header_bottom, text = f"Matt Cahill's Profile (This is You) {space} Facebook", font = cal18bold, fg = "white", background = "royalblue2")
        profilename.place(x = 0, y = 0)

        search = tk.Entry(sideframe_bottom)
        search.place(x=0,y=0)
        list = ["Profile", "Friends", "Photos", "Notes", "Groups", "Events", "Messages", "Account", "Privacy"]
        Profile = tk.Label(sideframe_bottom, text = f"My Profile", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 20)
        Profile = tk.Label(sideframe_bottom, text = f"My Friends", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 40)
        Profile = tk.Label(sideframe_bottom, text = f"My Photos", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 60)
        Profile = tk.Label(sideframe_bottom, text = f"My Notes", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 80)
        Profile = tk.Label(sideframe_bottom, text = f"My Groups", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 100)
        Profile = tk.Label(sideframe_bottom, text = f"My Events", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 120)
        Profile = tk.Label(sideframe_bottom, text = f"My Messages (7)", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 140)
        Profile = tk.Label(sideframe_bottom, text = f"My Account", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 160)
        Profile = tk.Label(sideframe_bottom, text = f"My Privacy", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 180)

        Profile = tk.Label(editbox, text = "View More Photos of Me", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 0)
        Profile = tk.Label(editbox, text = "Read Notes about Me", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 20)
        Profile = tk.Label(editbox, text = "Edit My Profile", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 40)
        Profile = tk.Label(editbox, text = "Edit My Picture", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 60)
        Profile = tk.Label(editbox, text = "Edit My Privacy", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 80)
        Profile = tk.Label(editbox, text = "Create a Profile Badge", fg = "cornflower blue", background = "white")
        Profile.place(x = 0, y = 100)

        tk.Label(contacts, text = "Matt Cahill", font = cal18bold, fg = "royalblue4", background = "white").place(x = 0, y = 10)
        tk.Label(contacts, text = "Facebook", background = "white").place(x = 0, y = 40)
        tk.Label(contacts, text = "Iowa State Alum", background = "white").place(x = 0, y = 60)
        tk.Label(contacts, text = "Silicon Valley, CA", background = "white").place(x = 0, y = 80)

        tk.Label(contacts, text = "Email:", background = "white", fg = "grey").place(x = 0, y = 110)
        tk.Label(contacts, text = "AIM Screenname:", background = "white", fg = "grey").place(x = 0, y = 125)
        tk.Label(contacts, text = "Mobile:", background = "white", fg = "grey").place(x = 0, y = 140)
        tk.Label(contacts, text = "Sex:", background = "white", fg = "grey").place(x = 0, y = 165)
        tk.Label(contacts, text = "Interested In:", background = "white", fg = "grey").place(x = 0, y = 180)

        tk.Label(contacts, text = "mcahill@facebook.com", background = "white", fg = "black").place(x = 130, y = 110)
        tk.Label(contacts, text = "lacuna arcana", background = "white", fg = "royalblue4").place(x = 130, y = 125)
        tk.Label(contacts, text = "319.378.1965", background = "white", fg = "black").place(x = 130, y = 140)
        tk.Label(contacts, text = "Male", background = "white", fg = "royalblue4").place(x = 130, y = 165)
        tk.Label(contacts, text = "Women", background = "white", fg = "royalblue4").place(x = 130, y = 180)

        tk.Label(dropdowns, text = f"▶ Mini-Feed{space}{space}             ", background = "light steel blue", fg = "royalblue4").place(x = 0, y = 0)
        tk.Label(dropdowns, text = f"▼ Personal Info{space}{space}        ", background = "light steel blue", fg = "royalblue4").place(x = 0, y = 25)

        tk.Label(dropdowns, text = "Political Views:", background = "white", fg = "grey").place(x = 0, y = 55)
        tk.Label(dropdowns, text = "Interests:", background = "white", fg = "grey").place(x = 0, y = 75)

        tk.Label(dropdowns, text = "Favorite Music:", background = "white", fg = "grey").place(x = 0, y = 120)
        tk.Label(dropdowns, text = "Favorite TV Shows:", background = "white", fg = "grey").place(x = 0, y = 240)
        tk.Label(dropdowns, text = "Favorite Movies:", background = "white", fg = "grey").place(x = 0, y = 270)
        tk.Label(dropdowns, text = "Favorite Quotes:", background = "white", fg = "grey").place(x = 0, y = 345)

        tk.Label(dropdowns, text = "Moderate", background = "White", fg = "royalblue4").place(x = 130, y = 55)
        tk.Label(dropdowns, text = "Web Design, Photography, Almost All Music, Tennis, Nintendo DS Lite", background = "White", fg = "royalblue4", 
                wraplength=300, justify = "left").place(x = 130, y = 75)
        tk.Label(dropdowns, text = "Zero 7, Air, Beatles, Imogen Heap, Acceptance, Coldplay, Massive Attack, Belle & Sebastian, Jurassic 5, Blackalicious, Björk, Scissor Sisters, Daft Punk, Theivery Corporation, BT, Beck, Wilco, Deathcab for Cutie, Utada Hikaru, Way Out West, Radiohead, The Streets, Cake, Chemical Brothers, Moby, Fischerspooner, High and Mighty Color",
                background = "White", fg = "royalblue4", wraplength=300, justify = "left").place(x = 130, y = 120)
        tk.Label(dropdowns, text = "Lost, Family Guy, Firefly, Bleach, Battlestar Galactica", background = "White", fg = "royalblue4", 
                wraplength=300, justify = "left").place(x = 130, y = 240)
        tk.Label(dropdowns, text = "Harold and Kumar Go to White Castle, The Incredibles, Zoolander, Kill Bill, Ferris Bueller's Day Off, Fight Club, Boondock Saints, Office Space, American Beauty, Stargate, Dogma, Super Troopers, Wayne's World, Ocean's Eleven, Primer", background = "White", fg = "royalblue4", 
                wraplength=300, justify = "left").place(x = 130, y = 270)
        tk.Label(dropdowns, text = '"Drama is life with all of the dull bits cut out" -Alfred Hitchcock', background = "White", fg = "black", 
                wraplength=300, justify = "left").place(x = 130, y = 345)
        #for justify https://stackoverflow.com/questions/37318060/how-to-justify-text-in-label-in-tkinter
        #tkinter wraplength https://www.tutorialspoint.com/python/tk_label.htm
tk.Label(root, text = "Log in to Facebook").pack()
user = tk.StringVar() 
user.set("")
passw = tk.StringVar()
passw.set("")
usernbox = tk.Entry(root, textvariable = user)
passbox = tk.Entry(root, textvariable = passw)
enter = tk.Button(root, text = "Login", command=lambda: open_page(user.get(), passw.get()))
usernbox.pack()
passbox.pack()
enter.pack()

root.mainloop()