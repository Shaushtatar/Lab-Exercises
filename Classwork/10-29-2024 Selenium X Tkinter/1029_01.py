'''An action chain allows you to automate basic movements, like double clicking,
moving the mouse to a place on the screen, pressing enter, and other basic
commands

They are used because some web pages require you to hover over an element 
before you can click, or maybe click on a drop-down menu to find some information
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

'''Goal for the code is to sort the data set by "Date Added", 
scrape the links to the data sets, then go to the next page.
'''

driver.get("https://catalog.data.gov/dataset?q=climate+change")

try:

    search_input = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "search-big")) #search bar
    )

    search_input.clear()
    search_input.send_keys("Food Desert") #typing in food desert instead of climate change
    search_input.send_keys(Keys.RETURN)

    menu = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "field-order-by"))
    )  


    actions = ActionChains(driver)
    actions.move_to_element(menu)
    # menu_item = driver.find_element(By.NAME, "sort")
    
    #action chain
    actions.click(menu).click(menu).perform()
    
    #it's always good to use WebDriverWait if you need to click on something
    date_added = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='field-order-by']/option[1]"))
    ).click()
    
    #let's scrape all the elements and links on this page
    #We can look for all a tags in an h3 tag using this syntax
    
    link = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/section[1]/div[2]/ul/li[1]/div/h3/a"))
    )
    actions.click(link).perform()

    desc_block = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(By.CLASS_NAME, "notes embedded-content")
    )

    '''
    all_links = driver.find_elements(By.CSS_SELECTOR, "h3 a")
    
    for i in all_links:
        link = i.get_attribute("href")
        print(link)
    
    #Now we'll scroll down & click on the next button
    next_page = driver.find_element(By.LINK_TEXT, "»")
    actions.move_to_element(next_page).click().perform()
    '''

    time.sleep(5)
    
finally:
    driver.quit()
