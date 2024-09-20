import requests
import json
import csv
lat = "42.098701"
lon = "-75.912537"

def get_weather(lat,lon):
    weather = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
    json_weather = weather.json()
    isolated_forecast = json_weather["properties"]["forecast"]
    forecast = requests.get(isolated_forecast).json()

    data_file = open("weather_forecasts.csv", "w", newline = "", encoding = "utf-8")
    csv_writer = csv.writer(data_file)
    csv_writer.writerow(["name","temperature","detailedForecast"])

    for section in forecast["properties"]["periods"]:
        day = section["name"]
        temp = section["temperature"]
        detail = section["detailedForecast"]
        csv_writer.writerow([day, temp, detail])

    data_file.close()

get_weather(lat,lon)


