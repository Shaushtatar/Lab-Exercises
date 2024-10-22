#using https://books.toscrape.com/catalogue/page-1.html as our practice website
from bs4 import BeautifulSoup
import requests
import html5lib
import csv
source = requests.get("https://books.toscrape.com/catalogue/page-1.html").text
soup = BeautifulSoup(source, "lxml")
#print(soup.prettify())

#What elements are needed to get title and price?
#Look for our "big box" which contains both title and price, and our small boxes and attributes
#which contain price and title distinctively
#big box: <article class="product_pod">
#book <h3><a href="" title= Book title (long) > Book title (short) </a>     .text
#<p class="price_color"> Price </p>

title_dict = {}

for i in soup.find_all("article", class_="product_pod"):
    #print(i.h3.a.text) -- this gets our (shortened) titles. Our long title is in an attribute in our <a>
    title = i.h3.a.get("title")
    #To get something in an attribute, we use the get method on the a attribute. 
    price = i.find("p", class_="price_color").text.strip("Â") #it was giving us that symbol so we are stripping Â

    title_dict[title] = price #putting it in a dictionary
    
print(title_dict)