from bs4 import BeautifulSoup
import re
import requests
n = input('Enter model of car:')
m = 'https://www.truecar.com/used-cars-for-sale/listings/' + n.lower()
p = requests.get(m).text
soup = BeautifulSoup(p,'html.parser')
cars = soup.find_all('div',attrs={'data-test':'cardContent'})
res = []
info = tuple()
del cars[20:34]
for i in cars:
    print(BeautifulSoup(i,'html.parser').find('span',attrs={'class':'truncate'}))