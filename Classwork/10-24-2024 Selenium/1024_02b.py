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
    main = WebDriverWait(driver, 5).until( 
    EC.presence_of_element_located((By.ID, "nav-sandbox")) 
    )
    
    sandbox = driver.find_element(By.ID, "nav-sandbox").click() 
    '''    
    for element in driver.find_elements(By.CSS_SELECTOR, "div.page"): 
        desc = element.find_element(By.TAG_NAME, "p").text 
        title = element.find_element(By.TAG_NAME, "h3").text 
        print(title, "|", desc)
    '''
    #Instead of going through the for loop, let's try clicking on our first link, "countries of the world"
    #<a href="/pages/simple/">Countries of the World: A Simple Example</a>
    countries = driver.find_element(By.XPATH, '//*[@id="pages"]/section/div/div/div/div[1]/h3/a').click()

    #You could also use "Link Text" with Countries of the World: A Simple Example
    #Or partial link text with "Countries of the World" or even "Countries". But make sure this is unique
    #If what you are looking by isn't unique, whatever instance shows up first will be picked



finally:
    driver.quit()
