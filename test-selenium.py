from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

def wasteTime(timeToWait):
    time.sleep(timeToWait+random.random()*3)

def wasteTimeClick(timeToWait):
    time.sleep(random.random()*timeToWait)

driver = webdriver.Firefox()

driver.get("https://www.indopremier.com/ipotnews/newsSmartSearch.php?code=BBCA")
wasteTime(3)

inputStartDate = driver.find_element(By.NAME, 'startDate')
wasteTime(1)
inputStartDate.send_keys(Keys.CONTROL + "a")
wasteTimeClick(2)
inputStartDate.send_keys(Keys.DELETE)
wasteTimeClick(2)
inputStartDate.send_keys('10/10/2022')
wasteTimeClick(2)
inputStartDate.send_keys(Keys.CONTROL + "a")
wasteTimeClick(2)
inputStartDate.send_keys(Keys.CONTROL + "c")
wasteTime(2)

inputEndDate = driver.find_element(By.NAME, 'endDate')
wasteTime(1)
inputEndDate.send_keys(Keys.CONTROL + "a")
wasteTimeClick(1)
inputEndDate.send_keys(Keys.DELETE)
wasteTimeClick(2)
inputEndDate.send_keys(Keys.CONTROL + "v")

wasteTime(2)

submitBtn = driver.find_element(By.XPATH, '//button[text()="GO"]')
submitBtn.click()
