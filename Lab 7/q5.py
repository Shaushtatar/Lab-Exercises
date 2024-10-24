#using https://books.toscrape.com/catalogue/page-1.html 
from bs4 import BeautifulSoup
import requests
import html5lib
import csv
source = requests.get("https://books.toscrape.com/catalogue/page-1.html").text
soup = BeautifulSoup(source, "lxml")
#print(soup.prettify())

title_dict = {}

for i in soup.find_all("article", class_="product_pod"):

    title = i.h3.a.get("title")
    #To get something in an attribute, we use the get method on the <a> attribute. 
    price = i.find("p", class_="price_color").text.strip("Â") #it was giving us that symbol so we are stripping Â

    title_dict[title] = price #putting it in a dictionary
    
print(title_dict)