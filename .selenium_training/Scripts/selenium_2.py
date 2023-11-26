from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.common.by import By
import pandas as pd
web = "https://www.audible.com/search"
path = r"C:\\Users\\User\Desktop\\Python_Program\\Scrapping_Practice\\.selenium_training\\msedgedriver.exe"

#Compulsory Code in Selenium 4.0
options = webdriver.EdgeOptions()
service = Service(path)

#Code to Disable the Devtools listening on ....
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#Open MS Edge webdriver and opening the website
driver = webdriver.Edge(service=service, options=options)
driver.get(web)
driver.maximize_window()

container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
products = container.find_element(By.XPATH, './li')

title=[]
author=[]
length=[]

for product in products:
    title.append(product.find_element(By.XPATH, "//h3[contains(@class, 'bc-heading')]").text)
    author.append(product.find_element(By.XPATH, "//LI[contains(@class, 'authorLabel')]").text)
    length.append(product.find_element(By.XPATH, "//LI[contains(@class, 'RUNTIMELabel')]").text)
    
driver.quit()
df = pd.DataFrame({'title':title,'author':author,'length':length})
df.to_csv('Selenium_2.csv', index=False)