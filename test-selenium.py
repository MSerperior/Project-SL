from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from bs4 import BeautifulSoup
import json
import pymongo as pm
from datetime import datetime, timedelta

def wasteTime(timeToWait):
    time.sleep(timeToWait+random.random()*3)


def wasteTimeClick(timeToWait):
    time.sleep(random.random()*timeToWait)


# Connect to the MongoDB server
client = pm.MongoClient('localhost', 27017)

# Connect to the database
db = client['Project_SL']

# Connect to the collection
coll = db['broker_summary']


driver = webdriver.Firefox()

driver.get("https://www.indopremier.com/ipotnews/newsSmartSearch.php?code=BBCA")
wasteTime(3)


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

    return driver.page_source

# input_date('10/10/2022')
# html = driver.page_source
# file = open("test.html", "w")
# file.write(html)


def read_html():
    file = open("test.html", "r")
    html = file.read()
    return html


def get_data(html, day):
    data = {
        'Top Buyer': {},
        'Top Seller': {},
        'T. Val': 0,
        'F. NVal': 0,
        'T. Lot': 0,
        'Avg': 0,
        'Date': day
    }
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

        data["Top Buyer"].setdefault(str(cols[4]), buyer)
        data["Top Seller"].setdefault(str(cols[4]), seller)
        # print(cols)

    tfoot = table.find('tfoot')
    foot_rows = tfoot.find_all('span')
    foot_rows = [ele.text.strip() for ele in foot_rows]
    # print(foot_rows)

    data["T. Val"] = money_to_int(foot_rows[0].split(' : ')[-1])
    data["F. NVal"] = money_to_int(foot_rows[1].split(' : ')[-1])
    data["T. Lot"] = money_to_int(foot_rows[2].split(' : ')[-1])
    data["Avg"] = money_to_int(foot_rows[3].split(' : ')[-1])
    # print(json.dumps(data, indent=2))
    return data


def money_to_int(money):
    if (money[-1] == 'K'):
        return int(float(money[:-1].replace(',', ''))*1000)
    elif (money[-1] == 'M'):
        return int(float(money[:-1].replace(',', ''))*1000000)
    elif (money[-1] == 'B'):
        return int(float(money[:-1].replace(',', ''))*1000000000)
    elif(money[-1] == 'T'):
        return int(float(money[:-1].replace(',', ''))*1000000000000)
    return int(money.replace(',', ''))

data = []
for i in range(1, 35):
    try :
        day = datetime.today()
        day = day.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=i)

        if (day.weekday() == 5 or day.weekday() == 6):
            continue
        query = {"Date": day}
        if (coll.find_one(query) != None):
            continue
        html = input_date(day.strftime("%m/%d/%Y"))
        data.append(get_data(html, day))
    except:
        print("Failed to get data on :" + day.strftime("%m/%d/%Y"))
        continue

try :
    coll.insert_many(data)
except:
    print("Failed to insert data")
client.close()


# get_data(read_html())
# print(money_to_int("96.5 M"))
# print(date(2022, 10, 31).strftime("%m/%d/%Y"))
# today = date.today()
# yesterday = today - timedelta(days=1)
# print(today.strftime("%m/%d/%Y"))
# print(yesterday.strftime("%m/%d/%Y"))
