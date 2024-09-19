import requests
import json

def latloninput():
    i = 0
    while i == 0:
        i = 1
        lat = input("Choose a latitude. The end latitude and longitude must be in the United States:")
        lon = input("Choose a longitude. The end longitude must be in the United States:")
        try:
            float(lat)
            float(lon)
        except: 
            ValueError
            print("Please enter numbers!")
            i = 0
    #https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python I used this for the idea to use try/except
    #lat = 42.09
    #lon = -75.01
    link = f"https://api.weather.gov/points/{lat},{lon}"
    return link



def get_address(latlonlink):
    weather = requests.get(latlonlink)
    json_weather = weather.json()
    try:
        status = json_weather["status"]
        if status == 404:
            print(json_weather["detail"])
    except:
        KeyError #Addresses in the United States do not get a "status", so a key error is desirable here
        addresslink = json_weather["properties"]["forecastOffice"]
        office = requests.get(addresslink)
        json_office = office.json()
        ad = json_office["address"]
        print(f"Mailing Address: {ad["streetAddress"]}, {ad["addressLocality"]}, {ad["addressRegion"]}, {ad["postalCode"]}")
x=0 #determines continuity of while loop
while True:
    get_address(latloninput())
    again = input("Press 1 to look up a new address. Press anything else to quit.")
    if again != "1":
        break