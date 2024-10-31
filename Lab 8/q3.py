from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://catalog.data.gov/dataset")

data_file = open("climatechange.csv", "w", newline = "", encoding = "utf-8")
csv_writer = csv.writer(data_file)
csv_writer.writerow(["Title","Description"])

try:

    search_input = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "search-big")) #search bar
    )

    search_input.clear()
    search_input.send_keys("Climate Change") 
    search_input.send_keys(Keys.RETURN)

    desc_block = driver.find_elements(By.CLASS_NAME, "dataset-content")
    for i in desc_block:
        title = (i.find_element(By.TAG_NAME, "a").text) #gets title
        description = (i.find_element(By.CLASS_NAME, "notes").text) #gets description
        csv_writer.writerow([title, description])
finally:
    driver.quit()
    data_file.close()
