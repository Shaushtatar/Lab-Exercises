from bs4 import BeautifulSoup
import requests
import html5lib
import csv

data_file = open("cats_media.csv", "w", newline = "", encoding = "utf-8")
csv_writer = csv.writer(data_file)
csv_writer.writerow(["Name","Hyperlink","Date", "Abstract"])

page = 1
while page < 6:
    source = requests.get(f"https://www.loc.gov/search/?q=cats&sp={page}").text
    soup = BeautifulSoup(source, "lxml")

    for i in soup.find_all("div", class_="description"):
        name = (i.find("span", class_="item-description-title").a.text.strip())
        url = (i.find("span", class_="item-description-title").a.get("href"))
        try:
            date = i.ul.find("li", class_="date").span.text #date and abstract were returning some missing text, so I added try-excepts to them
        except AttributeError:
            date = None
        try:
            abstract = i.find("span", class_="item-description-abstract").text.strip()
        except AttributeError:    
            abstract = None
        
        csv_writer.writerow([name, url, date, abstract])
    page += 1

data_file.close()