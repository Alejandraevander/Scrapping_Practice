# //tagName[@AttributName="Value"]
# contains() / starts-with()
# //tagName[@contains(@AttributeName, "Value")]
# //tagName[(expression 1) and (expression 2)]\
# // parent / single, . present, .. parent, //x/" all details in x
# Selenium can scrap website with dynamic content

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = "https://www.adamchoi.co.uk/overs/detailed"
path = r"C:\\Users\\User\Desktop\\Python_Program\\Scrapping_Practice\\.selenium_training\\msedgedriver.exe"

#Compulsory Code in Selenium 4.0
options = webdriver.EdgeOptions()
service = Service(path)

#Code to Disable the Devtools listening on ....
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#Open MS Edge webdriver and opening the website
service = Service(path)
driver = webdriver.Edge(service=service, options=options)
driver.get(website)

#To click on the  button of All Matches
all_matches_button = driver.find_element(By.XPATH,"//label[@analytics-event='All matches']")
all_matches_button.click()
dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text('Spain')
time.sleep(10)

matches = driver.find_elements(By.TAG_NAME,'tr')


#List to store data (Xpath start from 1 not 0)
date=[]
home_team=[]
score=[]
Country=[]

#Extracting the data
for match in matches:
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home_team.append(match.find_element(By.XPATH,'./td[2]').text)
    score.append(match.find_element(By.XPATH,'./td[3]').text)
    Country.append(match.find_element(By.XPATH,'./td[4]').text)

driver.quit()

#storing the data above
df = pd.DataFrame({'date': date, 'home_team':home_team, 'score':score, 'Country':Country})
df.to_csv('football_data.csv', index=False)
print(df)
