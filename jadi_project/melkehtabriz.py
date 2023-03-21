from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
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

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    
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
    # Pricing data[3] & per meter data[4]
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
    print(data,len(data))