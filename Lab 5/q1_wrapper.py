import requests
import json
def getjson():
    word = input("Choose a word:")
    word = word.lower()
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    dictword = requests.get(url)
    json_word = dictword.json()


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
#getjson()
#print(definitions(json_word))
#print("\n\n")
#print(pronunciation(json_word))
#print("\n\n")
#print(examples(json_word))
#print(wiktionaryurl(json_word))
