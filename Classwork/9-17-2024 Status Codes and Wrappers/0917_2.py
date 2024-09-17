from PIL import Image
import json
import requests
import urllib
key = "dMKHhSlhDIhsqwxjD6seruc3fl0akyhhetrSoQ8B"

def get_hyperlink(y,m,d):
    date = f"{y}-{m}-{d}"
    link = f"https://api.nasa.gov/planetary/apod?api_key={key}&date={date}"
    #Question mark starts our query
    #Ampersand adds new variables
    return link
def get_image(hyperlink):
    apod = requests.get(hyperlink)
    json_apod = apod.json()
    imurl = json_apod["url"]
    urllib.request.urlretrieve(imurl,"nasa.jpg")
    image = Image.open("nasa.jpg")
    return image
print(get_image(get_hyperlink("2004","03","07")))
