
import requests
import json
lat = 14.099
lon = -75.913
weather = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

#How to react to status codes
if weather.status_code == 200:
    print("Whatever")
    json_weather = weather.json
elif weather.status_code == 500:
    print("That location is not in the United States")

