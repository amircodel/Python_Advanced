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

# If you want to limit the number of scroll loads, add a limit here
scroll_limit = 1

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
main = []
for lnk in urls:
    del soup
    data = []
    soup = BeautifulSoup(requests.get(lnk).text,'html.parser')
    data.append(re.findall(r'\d+',lnk))
    outp = soup.find_all('div',attrs={'class':'text-infmlk col-6'})
    ex = [i.text for i in outp]
    if len(ex) == 11:
        ex.pop(9)
    print(ex)