from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#Let's use selenium to look something up on the browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")

try:
    main = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "q"))
    )
    #<textarea class="gLFyf" aria-controls="Alh6id" aria-owns="Alh6id" autofocus="" title="Search" value="" jsaction="paste:puy29d;" aria-label="Search" aria-autocomplete="both" aria-expanded="false" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" id="APjFqb" maxlength="2048" name="q" role="combobox" rows="1" spellcheck="false" data-ved="0ahUKEwiDxLbe56eJAxUzrokEHT82An8Q39UDCBA"></textarea>
    search_box = driver.find_element(By.NAME, "q") #name attribute of <textarea> on google page is "q"
    #The other options for searching using selenium with be class (gLFyf), by textarea itself, by element ID, and by Xpath
    search_box.send_keys("Binghamton University")

    search_box.send_keys(Keys.RETURN)
    
    
finally:
    driver.quit()
