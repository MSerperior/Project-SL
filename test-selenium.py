from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from bs4 import BeautifulSoup
import json

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

data = dict()

data['10/10/2022'] = {
    'Top Buyer': {},
    'Top Seller': {},
    'T. Val': 0,
    'F. NVal': 0,
    'T. Lot': 0,
    'Avg': 0,
}

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
    # print(headers)

    tbody = table.find('tbody')
    rows = tbody.find_all('tr')
    for row in rows:
        cols = row.find_all('td')

        cols = [ele.text.strip() for ele in cols]
        buyer = dict()
        buyer["Buyer"] = cols[0]
        buyer["B.Lot"] = money_to_int(cols[1])
        buyer["B.Val"] = money_to_int(cols[2])
        buyer["B.Avg"] = money_to_int(cols[3])
        seller = dict()
        seller["Seller"] = cols[5]
        seller["S.Lot"] = money_to_int(cols[6])
        seller["S.Val"] = money_to_int(cols[7])
        seller["S.Avg"] = money_to_int(cols[8])


        data["10/10/2022"]["Top Buyer"].setdefault(int(cols[4]), buyer)
        data["10/10/2022"]["Top Seller"].setdefault(int(cols[4]), seller)
        # print(cols)

    tfoot = table.find('tfoot')
    foot_rows = tfoot.find_all('span')
    foot_rows = [ele.text.strip() for ele in foot_rows]
    # print(foot_rows)

    data["10/10/2022"]["T. Val"] = money_to_int(foot_rows[0].split(' : ')[-1])
    data["10/10/2022"]["F. NVal"] = money_to_int(foot_rows[1].split(' : ')[-1])
    data["10/10/2022"]["T. Lot"] = money_to_int(foot_rows[2].split(' : ')[-1])
    data["10/10/2022"]["Avg"] = money_to_int(foot_rows[3].split(' : ')[-1])
    print(json.dumps(data, indent=2))
# print(float("35,661".replace(',', '')))

def money_to_int(money):
    if(money[-1] == 'M'):
        return int(float(money[:-1].replace(',', ''))*1000000)
    elif(money[-1] == 'B'):
        return int(float(money[:-1].replace(',', ''))*1000000000)
    return int(money.replace(',', ''))
    
get_data(read_html())
# print(money_to_int("96.5 M"))
