from bs4 import BeautifulSoup
import re
import requests
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test2"
)
cursor = mydb.cursor()
total = []
n = input('Enter Brand of car:')
n = n.lower()
m = 'https://www.truecar.com/used-cars-for-sale/listings/' + n
p = requests.get(m).text
soup = BeautifulSoup(p,'html.parser')
cars = soup.find_all('div',attrs={'data-test':'cardContent'})
del cars[20:34]
for i in cars:
    # list of a car info includes name , price , des.
    res = []
    # get and insert car name and model in res
    demo = []
    demo.extend(re.findall(f'[{n.capitalize()},{n.upper()}]+\s+\w+', i.get_text(separator=" ")))
    brand = demo[0]
    brand = brand.replace(' ','',2)
    res.append(brand)
    # get and insert car price in res
    price = re.sub(r'\[\'[Price,price]+\s\$|\,*|\'\]', '', str(re.findall(r'[Price,price]+\s\$\d+\,\d+\,*\d*\,*\d*', i.get_text(separator=" "))))
    res.append(int(price))
    # get and insert car des. in res
    des = re.sub(r'\[\'|\s|\,|miles\'\]', '', str(re.findall(r'\s\d+\,*\d*\s+miles', i.get_text(separator=" "))))
    res.append(int(des))
    total.append(tuple(res))
    #   END
stmt = "SHOW TABLES LIKE 'cars'"
cursor.execute(stmt)
isthere = cursor.fetchone()
if not isthere:
    sql01 = "CREATE TABLE cars (Model varchar(255), Price int, Miles int);"
    cursor.execute(sql01)
for car in total:
    cursor.execute("INSERT INTO cars (Model, Price, Miles) VALUES (%s, %s, %s)",car)
mydb.commit()