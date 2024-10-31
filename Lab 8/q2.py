from PIL import Image
import requests
import urllib

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
urllist = []
driver.get("https://www.wikipedia.org/")
def isjpeg_append(link):
    if link.endswith(".jpg"):
        #https://www.codecademy.com/resources/docs/python/strings/endswith I learned about this here
        urllist.append(link)
def get_url():
    
    try:
        main = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='searchInput']"))
        )
        search_box = driver.find_element(By.XPATH, "//*[@id='searchInput']") 
        search_box.send_keys("Cat")

        search_box.send_keys(Keys.RETURN)

        images = driver.find_elements(By.TAG_NAME, 'img')
        for image in images:
            isjpeg_append(image.get_attribute("src"))

    finally:
        time.sleep(1)

def randimgfinder(links):
    full_url = random.choice(links)
    imgurl = full_url[6:] #I was having trouble getting this to work, but when testing with a URL from the source code,
    try:                  #I noticed it worked when the https: was not included. So I truncated the string
        img_element = WebDriverWait(driver, 5).until( 
        EC.presence_of_element_located((By.XPATH, f"//img[@src='{imgurl}']"))
        )
        driver.find_element(By.XPATH, f"//img[@src='{imgurl}']").click()
        #I used this to get the right xpath https://stackoverflow.com/questions/4835891/extract-value-of-attribute-node-via-xpath
    finally:
        time.sleep(1)
        return full_url
        

def save_image(full_url):
    urllib.request.urlretrieve(full_url,"cat_image.jpg")
    image = Image.open("cat_image.jpg")
    image.show()



get_url()
save_image(randimgfinder(urllist))

driver.quit()