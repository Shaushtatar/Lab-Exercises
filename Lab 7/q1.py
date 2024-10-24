#using https://tedboy.github.io/bs4_doc/8_output.html
from bs4 import BeautifulSoup
import requests
import html5lib

source = requests.get("https://tedboy.github.io/bs4_doc/8_output.html").text
soup = BeautifulSoup(source, "lxml")
for i in soup.find_all("h1"):
    print(i.text.strip("¶")) #it had that weird symbol for some reason
