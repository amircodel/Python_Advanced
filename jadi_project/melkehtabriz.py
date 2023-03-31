from bs4 import BeautifulSoup
import requests
import re
import mysql.connector
import time
from datetime import datetime
start_time = datetime.now()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
)
cursor = mydb.cursor()
def loading():
    bar = ['L','LO','LOA','LOAD','LOADI','LOADIN','LOADING','LOADING.','LOADING..','LOADING...']
    i = 0
    while i < len(bar):
        print(bar[i % len(bar)], end="\r")
        time.sleep(0.1)
        i += 1
    print('          ',end='\r')
    time.sleep(0.1)
url = 'https://ap-api.melketabriz.com/api/v1/property?status_sell=614ed62da50555f0a54c1eca&status_property=614edc35a50555f0a54c1f12&category_property%5B%5D=614ee704a50555f0a54c227d&show_all=&page={}'
homes = []
urls = []
for page in range(1,27):
    response = requests.get(url.format(page)).json()
    homes.extend(response['data'][i]['code'] for i in range(len(response['data'])))
length = len(homes)
for code in homes:
    urls.append('https://melketabriz.com/p/%i'%code)
print('Please wait until receiving Data; This process will probably take %s minutes, However depends on your internet condition and the source server too'%(int(length*1.1190)//60))
print('\n')
main = []
for lnk in urls:
    loading()
    data = []
    soup = BeautifulSoup(requests.get(lnk).text,'html.parser')
    ex = soup.find_all('div',attrs={'class':'text-infmlk'})
    data.extend([i.text for i in ex])
    try:
        if len(ex) == 13:
            data.pop(2)
        # Code of notice data[0]
        # Area data[1]
        # Meterage data[2]
        data[2] = float(data[2])
        # Pricing data[3] & permeter data[4]
        data[3] = int(''.join(re.findall(r'\d+',data[3])))
        data.insert(4,int(data[3]//data[2]))
        # floor data[5]
        # Rooms data[6]
        data[6] = int(data[6])
        # Total floors data[7]
        data[7] = int(data[7])
        # Homes per one floor data[8]
        data[8] = int(data[8])
        # Buliding year data[9]
        data[9] = int(re.findall(r'\d+',data[9])[0])
        # Situation data[10]
        # Type of building data[11]
        # type of documentry data[12]
        main.append(tuple(data))
    except:
        pass
stmt = "SHOW TABLES LIKE 'melkehtabriz'"
cursor.execute(stmt)
isthere = cursor.fetchone()
if not isthere:
    sql01 = "CREATE TABLE melkehtabriz (Code VARCHAR(255), Area VARCHAR(255), Meterage FLOAT, Pricing BIGINT, PPM INT, Floor VARCHAR(255), Rooms INT, Allfloors INT, HPF INT, old INT, Situation VARCHAR(255), TypeBuilding VARCHAR(255), TypeDocumentry VARCHAR(255));"
    cursor.execute(sql01)
for home in main:
    sql02 = f"SELECT * FROM melkehtabriz WHERE Code LIKE '{home[0]}';"
    cursor.execute(sql02)
    if cursor.fetchone():
        cursor.execute(f"DELETE FROM melkehtabriz WHERE Code LIKE '{home[0]}';")
    cursor.execute(f"INSERT INTO melkehtabriz (Code, Area, Meterage, Pricing, PPM, Floor, Rooms, Allfloors, HPF, old, Situation, TypeBuilding, TypeDocumentry) VALUES {home}")
mydb.commit()
end_time = datetime.now()
print('Done, Duration: {}'.format(end_time - start_time))