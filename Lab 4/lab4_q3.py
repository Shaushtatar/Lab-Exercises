#I chose to use the Pokemon API
import requests
import json
import urllib
from PIL import Image
#base url: https://pokeapi.co/api/v2
#main website: https://pokeapi.co
#documentation: https://pokeapi.co/docs/v2
#First request: returns a json on Snorlax based on the suffix /pokemon/snorlax
pokemon1 = requests.get("https://pokeapi.co/api/v2/pokemon/snorlax")
json_pkmn1 = pokemon1.json()
#print(json_pkmn1)
#You can use this same path with abilities and other qualities of pokemon that are not a pokemon themselves

pokemon2 = requests.get("https://pokeapi.co/api/v2/ability/sturdy")
json_pkmn2 = pokemon2.json()

#Let's create a function returning a pokemon's sprite to us
pokedex = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
json_pkdx = pokedex.json()
#pokemon?limit=100000&offset=0 is what I found on the site for getting a full list of Pokemon
#When you just put /pokemon it only lists the first few, so ?limit=100000 queries for a list with
#a longer maximum amount
poke_choice = ""
dexnames = []
for i in json_pkdx["results"]:
    dexnames.append(i["name"])
while poke_choice not in dexnames:
    poke_choice = input("Choose your Pokemon:")
    poke_choice = poke_choice.lower()
    #The dex is all lowercase.
    if poke_choice not in dexnames:
        print("Enter a Pokemon in the pokedex with proper formatting.")
pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_choice}")
json_pkmn = pokemon.json()
sprite = json_pkmn["sprites"]["front_default"]
urllib.request.urlretrieve(sprite,f"pokemonsprite.jpg") #from what we did on 9/17
image = Image.open("pokemonsprite.jpg")
image.show()