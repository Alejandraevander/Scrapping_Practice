# //tagName[@AttributName="Value"]
# contains() / starts-with()
# //tagName[@contains(@AttributeName, "Value")]
# //tagName[(expression 1) and (expression 2)]\
# // parent / single, . present, .. parent, //x/" all details in x
# Selenium can scrap website with dynamic content

from selenium import webdriver

website = "https://www.adamchoi.co.uk/overs/detailed"
path = r"C:\Users\r14ale\Desktop\Selenium\.selenium_training\msedgedriver.exe"

driver = webdriver.Edge(path)
driver.get(website)

driver.quit()

