import requests
import json
key = "46062957-c701818c8c9fe048cfad924c0"
pics = requests.get(f"https://pixabay.com/api?key={key}&q=public+parks")
#https://pixabay.com/api/docs/
json_pics = pics.json()
park_dict = {}
for i in json_pics["hits"]:
    park_dict[i["id"]] = i["largeImageURL"]

print(park_dict)