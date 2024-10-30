from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.scrapethissite.com/")

try:
    main = WebDriverWait(driver, 5).until( #wait until we find sandbox -- we give the 'puter 5 seconds
    EC.presence_of_element_located((By.ID, "nav-sandbox")) #open site and navigate to the item with the id sandbox
    )
    
    sandbox = driver.find_element(By.ID, "nav-sandbox").click() #if we had slow internet connection, this might not work
    
    for element in driver.find_elements(By.CSS_SELECTOR, "div.page"): #"big box" is div page
        desc = element.find_element(By.TAG_NAME, "p").text #gets description
        title = element.find_element(By.TAG_NAME, "h3").text #gets title
        print(title, "|", desc)
    
finally:
    driver.quit()
