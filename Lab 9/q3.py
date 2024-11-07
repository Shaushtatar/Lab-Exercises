import requests
import json
import tkinter as tk
import textwrap
def guiprint(x):
    for i in x:
        printable = "\n".join(textwrap.wrap(str(i),50))
        result = tk.Label(root, text = printable)
        #I used this https://stackoverflow.com/questions/2058925/how-can-i-break-up-this-long-line-in-python to help make it presentable
        #I also separated the list elements into their own labels, as all of the functions return a list 
        result.pack()

def getjson(word):
    word = word.lower()
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    dictword = requests.get(url)
    json_word = dictword.json()
    return json_word


def definitions(jsonword):
    deflist = []
    try: 
        for i in jsonword[0]["meanings"]:
            for x in i["definitions"]:
                deflist.append(f"|{x["definition"]}|") #the bars help distinguish definitions
        return deflist
    except(KeyError): #jsonword index for non-words will return a key error because it doesn't have the same format
        print("You entered a word not in the dictionary.")
        return ""
    

def pronunciation(jsonword):
    pronlist = []
    try: 
        for x in jsonword[0]["phonetics"]:
            if "text" in x:
                pronlist.append(x["text"])
        return pronlist
    #formatted in the form of a list because the different pronunciations don't have any particular indices attatched to them
    #jsonword[0]["phonetics"] is the list containing all the elements in phonetics, but I only want text
    #so since the elements are dictionaries, I clarify I want only x["text"]
    except(KeyError):
        print("You entered a word not in the dictionary.")
        return ""
    

def examples(jsonword):
    xamplist = []
    try: 
        for i in jsonword[0]["meanings"]:
            for x in i["definitions"]:
                if "example" in x: #have to do this because some don't have examples
                    xamplist.append(f"|{x["example"]}|")
        return xamplist
    except(KeyError): 
        print("You entered a word not in the dictionary.")
        return ""
    

def wiktionaryurl(jsonword):
    try:
        return jsonword[0]["sourceUrls"]
    except(KeyError):
        print("You entered a word not in the dictionary.")
        return ""
    

root = tk.Tk()
root.title("Dictionary App")
root.geometry("500x500") 

entry = tk.StringVar() 
entry.set("")   
prompt = tk.Label(root, text = "Type in a word:")
entrybox = tk.Entry(root, textvariable = entry)
defbtn = tk.Button(root, text = "Definition", command = lambda: guiprint(definitions(getjson(entry.get()))))
pronbtn = tk.Button(root, text = "Pronunciation", command = lambda: guiprint(pronunciation(getjson(entry.get()))))
exbtn = tk.Button(root, text = "Examples", command = lambda: guiprint(examples(getjson(entry.get()))))
urlbtn = tk.Button(root, text = "Wiktionary Url", command = lambda: guiprint(wiktionaryurl(getjson(entry.get()))))
test = tk.Button(root, text = "X", command = lambda: guiprint(entry.get()))

prompt.pack()
entrybox.pack()
defbtn.pack()
pronbtn.pack()
exbtn.pack()
urlbtn.pack()
test.pack()

root.mainloop()