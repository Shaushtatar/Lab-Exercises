import requests
import json
country_titles = requests.get("https://date.nager.at/api/v3/AvailableCountries")
json_ct = country_titles.json()
abrvlist = []
hdlist = []
for i in json_ct: #We have to index through AvailableCountries,
                  #because that json contains all of the country codes we need for our get query
    holiday = requests.get(f"https://date.nager.at/api/v3/publicholidays/2024/{i["countryCode"]}")
    json_holiday = holiday.json()
    hdlist.append({i["name"] : len(json_holiday)})

    '''The json for holidays was actually in the form of a list,
    with each holiday being an element of the list, so I realized I could just use the
    length method to find the amount of holidays, and link it to the country's
    name with a dictionary.'''

print(hdlist)