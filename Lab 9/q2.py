import tkinter as tk
import random
import tkinter.font as tkFont
#https://stackoverflow.com/questions/56735255/cannot-import-tkfont
#tkDocs documentation was not working 

def compat(person1, person2):
    p1list = list(person1)
    p1set = set(p1list)
    p2list = list(person2)
    p2set = set(p2list)
    #Had to refresh myself on this https://stackoverflow.com/questions/15768757/how-to-construct-a-set-out-of-list-items-in-python 
    sameletters = 0
    for i in p1set:
        if i in p2set:
            sameletters +=1
    compatibility = sameletters / ((len(p1set) + len(p2set)) / 2) 
#Compatibility is determined by the ratio between shared unique letters in the names and the average amount of unique letters in both names
    noise = random.randint(95,105) / 100
    compatibility_randomized = round(((compatibility*noise)*100)%100, 3)
    #Opposites attract, so if two people have a randomized compatibility score over 100 then
    #they are considered too similar, and their compatibility loses 100 points (by the modulo operator)
    score = tk.Label(root, text = compatibility_randomized, font = times32, background = "pink", foreground = "deep pink")
    tk.Label(root, text = f"{person1} and {person2} are", font = times13, background = "pink", foreground = "deep pink").grid()
    score.grid()
    tk.Label(root, text = "percent compatible.", font = times13, background = "pink", foreground = "deep pink").grid()
    entry_p1.delete(0, "end")
    entry_p2.delete(0,"end")

root = tk.Tk()
root.title("Love Calculator")
root.geometry("400x400")
root.configure(background='pink')
#https://stackoverflow.com/questions/2744795/background-color-for-tk-in-python I used this
#I was confused how to make the background of the whole root a certain color and not just a button

times18 = tkFont.Font(family = "times", size = 18)
#https://tkdocs.com/shipman/fonts.html 
times13 = tkFont.Font(family = "times", size = 14)
times32 = tkFont.Font(family = "times", size = 30)


title = tk.Label(root, text = "( ͡° ͜ʖ ͡°) ♡♡ Love Calculator ♡♡ ( ͡° ͜ʖ ͡°)", font = times18, background = "pink", foreground = "deep pink")
subtitle = tk.Label(root, text = "Enter your name and your partner's \n name to determine your compatibility", font = times13, background = "pink", foreground = "deep pink")

p1 = tk.StringVar() 
p1.set("")
p2 = tk.StringVar()
p2.set("")

entry_p1 = tk.Entry(root, textvariable = p1) 
entry_p2 = tk.Entry(root, textvariable = p2)

button = tk.Button(root, text = "Try Pairing", font = times18, background = "pink", foreground = "deep pink", 
                   command = lambda: compat(p1.get(), p2.get()))

title.grid()
subtitle.grid()
entry_p1.grid()
tk.Label(text = "+", font = times18, background = "pink", foreground = "deep pink").grid()
entry_p2.grid()
tk.Label(text = "\n", background = "pink").grid()
button.grid()

#I tried for about an hour and a half to make this on one row as seen in the picture, but for some reason
#the space between entries and between the entries and the + was always way too big and I could find no way to center it and have them close.
#My previous codes have always had far smaller grid cells.



root.mainloop()