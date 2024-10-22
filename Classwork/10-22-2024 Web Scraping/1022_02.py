from bs4 import BeautifulSoup
import requests
import html5lib
import csv

source = requests.get("https://www.scrapethissite.com/pages/simple/").text
soup = BeautifulSoup(source, "lxml")

for section in soup.find_all("div", class_="col-md-4 country"):
    title = section.h3.text.strip()
    capital = section.find("span", class_="country-capital").text.strip()
   
    try:
        population = section.find("span", class_="country-population").text.strip()
    except AttributeError:
        population = "No data listed"
   
    area = section.find("span", class_="country-area").text.strip()

    print(title, capital, population, area)
