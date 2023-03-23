from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
)
cursor = mydb.cursor()
# Headless/incognito Chrome driver  
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument('headless')
driver = webdriver.Chrome(executable_path='CHROMEDRIVER_PATH',chrome_options=chrome_options)

driver.get('https://melketabriz.com/search?status_sell=614ed62da50555f0a54c1eca&status_property=614edc35a50555f0a54c1f12&category_property=614ee704a50555f0a54c227d&#!')

# Set sleep time for the page to load on scroll
SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

# If you want to limit the number of scroll loads, add a limit here
scroll_limit = 2

count = 0
while True and count < scroll_limit:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    count += 1

sleep(2) 

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
homeurl = soup.find_all('span',attrs={'class':'code-mlk'})
homes = []
urls = []
for home in homeurl:
    homes.append(home.get_text())
for code in homes:
    c = homes[homes.index(code)]
    c = c.strip('کد: ')
    urls.append('https://melketabriz.com/p/%s'%c)
del home
main = []
for lnk in urls:
    del soup
    data = []
    soup = BeautifulSoup(requests.get(lnk).text,'html.parser')
    # data.extend(re.findall(r'\d+',lnk))
    ex = soup.find_all('div',attrs={'class':'text-infmlk'})
    data.extend([i.text for i in ex])
    if len(ex) == 13:
        data.pop(2)
    # Code of notice data[0]
    # Area data[1]
    # Meterage data[2]
    data[2] = float(data[2])
    # Pricing data[3] & permeter data[4]
    data[3] = int(''.join(re.findall(r'\d+',data[3])))
    data.insert(4,int(data[3]//data[2]))
    # Homes per one floor data[5]
    # Rooms
    data[6] = int(data[6])
    # Total floors
    data[7] = int(data[7])
    # floor of the home
    data[8] = int(data[8])
    # Buliding year
    data[9] = int(re.findall(r'\d+',data[9])[0])
    # Situation data[10]
    # Type of building data[11]
    # type of documentry data[12]
    main.append(tuple(data))
stmt = "SHOW TABLES LIKE 'melkehtabriz'"
cursor.execute(stmt)
isthere = cursor.fetchone()
if not isthere:
    sql01 = "CREATE TABLE melkehtabriz (Code VARCHAR(255), Area VARCHAR(255), Meterage FLOAT, Pricing INT, PPM INT, HPF VARCHAR(255), Rooms INT, Allfloors INT, Floor INT, old INT, Situation VARCHAR(255), TypeBuilding VARCHAR(255), TypeDocumentry VARCHAR(255));"
    cursor.execute(sql01)
for home in main:
    sql02 = f"SELECT * FROM melkehtabriz WHERE Code LIKE '{home[0]}';"
    cursor.execute(sql02)
    if cursor.fetchone():
        cursor.execute(f"DELETE FROM melkehtabriz WHERE Code LIKE '{home[0]}';")
    cursor.execute("INSERT INTO melkehtabriz (Code, Area, Meterage, Pricing, PPM, HPF, Rooms, Allfloors, Floor, old, Situation, TypeBuilding, TypeDocumentry) VALUES (%s, %s, %f, %i, %i, %s, %i, %i, %i, %i, %s, %s, %s);" %home)
mydb.commit()