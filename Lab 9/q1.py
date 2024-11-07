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

driver.get("https://www.binghamton-ny.gov/home")

gov = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="dropdownrootitem3"]/a')))
depts = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="dropdownrootitem3"]/div/div/ul[1]/li/a')))


actions = ActionChains(driver)
actions.move_to_element(gov)
actions.click(gov).click(depts).perform()


pcs = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="leftNav_2_0_127"]/ul/li/ul/li[14]/a[2]'))) #path to the "+" sign on Personnel/Civil Service
employment = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="leftNav_2_0_127"]/ul/li/ul/li[14]/ul/li/a')))
#The following is from the given guide on scraping tables, https://www.geeksforgeeks.org/scrape-table-from-website-using-python-selenium/ 
actions.click(pcs).click(employment).perform()
rows = 1 + len(driver.find_elements(By.XPATH, '//*[@id="ColumnUserControl4"]/div[2]/table/tbody/tr'))
columns = len(driver.find_elements(By.XPATH, '//*[@id="ColumnUserControl4"]/div[2]/table/tbody/tr[1]/td'))

data_file = open("jobs.csv", "w", newline = "", encoding = "utf-8")
csv_writer = csv.writer(data_file)
csv_writer.writerow(["Job", "Type", "Application Deadline", "Salary"])

for r in range(2, rows+1): 
    entry = []
    for p in range(1, columns+1):            
        value = driver.find_element(By.XPATH, 
            f'//*[@id="ColumnUserControl4"]/div[2]/table/tbody/tr[{str(r)}]/td[{str(p)}]').text 
        entry.append(value)
    csv_writer.writerow(entry)
data_file.close()
    
        