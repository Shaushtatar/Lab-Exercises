#basic text widget
import tkinter as tk
root = tk.Tk()
root.title("Text Widget practice")
root.geometry("500x500")

saved_text = tk.StringVar()

def insert_text(text): #only used when creating default text
    test_widget.insert("1.0", text)
    #adding the tag to the text
    test_widget.tag_add("center", "1.0", "end")

def clear_text():
    test_widget.delete("1.0", "end")
    test_widget.tag_add("center", "1.0", "end")
    
def save_text():
    saved_text = test_widget.get("1.0", "end-1c")
    tk.Label(root, text=saved_text).pack()

def center_text(event=None):
    test_widget.tag_add("center", "1.0", "end")  

#wrap parameter allows us to wrap text by words
#other options are "none" or "char"
test_widget = tk.Text(root, font = ("Helvitica", "16"),
                  height=10, width=25, wrap ="word") #wrap determines when the text box starts a new line. 
test_widget.pack()

#establishing a tag that is called "center" that center justifies
test_widget.tag_configure("center", justify="center")

#binding. argument 1 = what you want to bind it to, 
#argument 2 = what function you want to tie it to
#this binds to any key released on the keyboard
test_widget.bind("<KeyRelease>", center_text) #<KeyRelease> is an event. It is something your 'puter is listening for blud

erase_button = tk.Button(root, text="Erase Text", command=clear_text)
erase_button.pack(pady=20) 

save_button = tk.Button(root, text="Save your text", command=save_text)
save_button.pack(pady=20)

insert_text("This is my initial text. I am trying out my Text widget for the first time!")

root.mainloop()



