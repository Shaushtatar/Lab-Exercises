import requests
import json
lat = "42.09"
lon = "-75.91"

weather = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
json_weather = weather.json()
print(json_weather)