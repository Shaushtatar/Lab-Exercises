#using https://en.wikipedia.org/wiki/Binghamton,_New_York
from bs4 import BeautifulSoup
import requests
import html5lib
import csv

source = requests.get("https://en.wikipedia.org/wiki/Binghamton,_New_York").text
soup = BeautifulSoup(source, "lxml")

data_file = open("citations.csv", "w", newline = "", encoding = "utf-8")
csv_writer = csv.writer(data_file)
csv_writer.writerow(["Citation"]) #csv columns

for i in soup.find_all("ol", class_="references"):
    for j in i.find_all("span", class_="reference-text"):
        csv_writer.writerow([j.text])

data_file.close()