#To find an xpath, you simply right click the element in an "inspect element" tab
#then click copy --> copy xpath
#https://www.scrapethissite.com/pages/
#If we inspect our "Hockey Teams" link, and copy the xpath of the highlighted section, we get:
#//*[@id="pages"]/section/div/div/div/div[2]/h3/a

#Use the full xpath if:
#You need to precisely target an element
#The full xpath cannot accidentally grab anything else
#It's the direct path to the element you want

#Use the relative xpath if:
#Uou want something more concise 
#You know that there are not other identical elements on the page

#You can use selenium to find elements by id, name, xpath, link, etc etc
#py -m pip install selenium
#py -m pip install webdriver-manager
#=====================================================================================
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#These three imports are almost always going to be necessary when working with selenium
#=====================================================================================
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#These lines are not as central, but we use them a lot, so it's a good idea to import them
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#=====================================================================================
service = Service(ChromeDriverManager().install()) #
driver = webdriver.Chrome(service=service) #

driver.get("https://www.google.com") #     These first three lines of code (past imports) are usually necessary 
#=====================================================================================

print(driver.title)

driver.quit()
