from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from bs4 import BeautifulSoup


def wasteTime(timeToWait):
    time.sleep(timeToWait+random.random()*3)


def wasteTimeClick(timeToWait):
    time.sleep(random.random()*timeToWait)

# driver = webdriver.Firefox()

# driver.get("https://www.indopremier.com/ipotnews/newsSmartSearch.php?code=BBCA")
# wasteTime(3)


def input_date(date):
    inputStartDate = driver.find_element(By.NAME, 'startDate')
    wasteTime(1)
    inputStartDate.send_keys(Keys.CONTROL + "a")
    wasteTimeClick(2)
    inputStartDate.send_keys(Keys.DELETE)
    wasteTimeClick(2)
    inputStartDate.send_keys(date)
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

# input_date('10/10/2022')
# html = driver.page_source
# file = open("test.html", "w")
# file.write(html)


def read_html():
    file = open("test.html", "r")
    html = file.read()
    return html


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(
        'table', attrs={'class': 'table table-summary table-hover noborder nm'})
    thead = table.find('thead')
    headers = thead.find_all('th')
    headers = [ele.text.strip() for ele in headers]
    print(headers)

    tbody = table.find('tbody')
    rows = tbody.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        print(cols)

    tfoot = table.find('tfoot')
    foot_rows = tfoot.find_all('span')
    foot_rows = [ele.text.strip() for ele in foot_rows]
    print(foot_rows)


data = dict()

data['10/10/2022'] = {
    'Top Buyer': {},
    'Top Seller': {},
    'T. Val': 0,
    'F. NVal': 0,
    'T. Lot': 0,
    'Avg': 0,
}


get_data(read_html())
