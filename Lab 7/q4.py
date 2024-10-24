#using https://quotes.toscrape.com/
from bs4 import BeautifulSoup
import requests
import html5lib
import csv

source = requests.get("https://quotes.toscrape.com/").text
soup = BeautifulSoup(source, "lxml")

data_file = open("quotes.csv", "w", newline = "", encoding = "utf-8")
csv_writer = csv.writer(data_file)
csv_writer.writerow(["Quote", "Author"]) #csv columns
for i in soup.find_all("div", class_="quote"):
    csv_writer.writerow([i.span.text, i.small.text]) #small contains the author, span contains the quote

data_file.close()