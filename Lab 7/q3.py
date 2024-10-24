#using https://tedboy.github.io/bs4_doc/1_quick_start.html
from bs4 import BeautifulSoup
import requests
import html5lib

source = requests.get("https://tedboy.github.io/bs4_doc/1_quick_start.html").text
soup = BeautifulSoup(source, "lxml")
j = 1
for i in soup.find_all("div", class_="highlight-python"):
    if j == 2:
        codelist = i.text.split('\n')[4:]
        for line in codelist:
            print(line)
    j += 1
#prints only the second div with class highlight-python, which is the one we want
#I learned the method of removing the top lines from here:
#https://stackoverflow.com/questions/30833409/python-deleting-the-first-2-lines-of-a-string