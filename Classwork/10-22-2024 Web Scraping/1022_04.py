#But le what if we want to do this on multiple pages?
#Look at the HTML for our bookstoscrape. We can use a while loop to go through the pages

#Let's slightly modify 1022_03.py code
from bs4 import BeautifulSoup
import requests
import html5lib
import csv

title_dict = {} #we want all 10 pages in the same dictionary so we declare this before while loop

page = 1
while page != 11:
    source = requests.get(f"https://books.toscrape.com/catalogue/page-{page}.html").text
    soup = BeautifulSoup(source, "lxml")

    for i in soup.find_all("article", class_="product_pod"):
        title = i.h3.a.get("title")
        price = i.find("p", class_="price_color").text.strip("Â")
        title_dict[title] = price
    page += 1

print(title_dict)