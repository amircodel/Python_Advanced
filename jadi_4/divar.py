import requests
from bs4 import BeautifulSoup
import re
x = requests.get('https://divar.ir/s/tehran').text
soup = BeautifulSoup(x,'html.parser')
divars = soup.find_all('div',attrs={'class':'kt-post-card__body'})
lst = []
res = []
for i in divars:
    lst.append(i.get_text(separator=" ").replace(',',''))
for i in lst:
    l = re.split(r'\W+',i)
    if 'توافقی' in l:
        res.append(i)
for i in res:
    print(i)