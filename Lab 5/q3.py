import requests
import json
import random
from PIL import Image
import urllib
countrylist = []
url = "https://restcountries.com/v3.1/independent"
countries = requests.get(url)
json_countries = countries.json()
for i in json_countries:
    countrylist.append(i["name"]["common"])

points = 0
def capitalgame(): 
    countryname = random.choice(countrylist)  
    qcountry = requests.get(f"https://restcountries.com/v3.1/name/{countryname}")
    json_qcountry = qcountry.json()
    guess = input(f"What is the capital of {countryname}?")
    if guess.lower() == json_qcountry[0]["capital"][0].lower():
        print("Good choice! You get 4 pts.")
        return 4
    else: 
        print("Incorrect. The correct answer was " + json_qcountry[0]["capital"][0])
        return 0
def islandlocked(): 
    countryname = random.choice(countrylist)  
    qcountry = requests.get(f"https://restcountries.com/v3.1/name/{countryname}")
    json_qcountry = qcountry.json()
    guess = None
    while guess not in ["Y", "N"]:
        guess = input(f"Is {countryname} landlocked? (Y/N)")
        guess = guess.upper()
        if guess == "N":
            boolguess = False
        elif guess == "Y":
            boolguess = True
        else:
            print("Please enter a valid option.")

    if boolguess == json_qcountry[0]["landlocked"]:
        print("Good choice! You get 2 pts.")
        return 2
    else: 
        print("You are incorrect.")
        return 0

def flaggame():
    countryname = random.choice(countrylist)  
    qcountry = requests.get(f"https://restcountries.com/v3.1/name/{countryname}")
    json_qcountry = qcountry.json()
    imurl = json_qcountry[0]["flags"]["png"]
    urllib.request.urlretrieve(imurl, "flag_game_flag.jpg")
    image = Image.open("flag_game_flag.jpg")
    image.show()
    guess = input("What country is this?")
    if guess.lower() == countryname.lower():
        print("You got it! You get 3 pts.")
        return 3
    else:
        print("Sorry, the correct answer was " + countryname)
        return 0


def natllang():
    countryname = random.choice(countrylist)  
    qcountry = requests.get(f"https://restcountries.com/v3.1/name/{countryname}")
    json_qcountry = qcountry.json()
    guess = input(f"What is a language of {countryname}?")
    langlist = [x.lower() for x in json_qcountry[0]["languages"].values()] 
    #the languages have to be lowercased, they start out with uppercased first letters of words
    #https://www.geeksforgeeks.org/python-dictionary-values/ this helped me
    if guess.lower() in langlist:
        print("Good choice! You get 1 pt.")
        return 1
    else:
        print("You are incorrect. Here are the correct answers: " + str(langlist))
        return 0


def game():
    cont = True
    while cont == True:
        points = 0
        points = points + natllang()
        points = points + islandlocked()
        points = points + flaggame()
        points = points + capitalgame() #higher point games are later in the game
        print(f"You scored {points} out of 10.") #1+2+3+4

        choice = None
        while choice not in ["Y", "N"]:
            choice = input("Play again? (Y/N)")
            choice = choice.upper()
            if choice == "N":
                cont = False
            elif choice == "Y":
                cont = True
            else:
                print("Please enter a valid option.")
        
game()