from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

#Website to Scrap and driver location
web = "https://twitter.com/search?q=python&src=typed_query"
path = r"C:\\Users\\r14ale\\Desktop\\Scrapping_Practice\\.selenium_training\\msedgedriver.exe"

#Compulsory Code in Selenium 4.0
options = webdriver.EdgeOptions()
service = Service(path)

#Code to Disable the Devtools listening on ....
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument("--headless=new")
options.add_argument("windows-size=1920x1080")
#Open MS Edge webdriver and opening the website
driver = webdriver.Edge(service=service, options=options)
driver.get(web)

#To Scroll Infinite Scrolling
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    else:
        last_height = new_height
login = driver.find_element(By.XPATH, "//a[@href='/login']")

//input[@name='text']