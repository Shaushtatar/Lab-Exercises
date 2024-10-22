#We're using this site for scaping examples https://www.scrapethissite.com/pages/
#installing html5lib, lxml, bs4: py -m pip install
from bs4 import BeautifulSoup
import requests
import html5lib
import csv
source = requests.get("https://www.scrapethissite.com/pages/").text
soup = BeautifulSoup(source, "lxml")
#print(soup)
#lxml is a library that helps us process html in Python
base_link = "https://www.scrapethissite.com/"
for i in soup.find_all("h3", class_="page-title"):
    text = i.a.text #gets me the text
    link = i.a.get("href") #gets me the link
    full_link = base_link + link
    print(text, link, full_link)
