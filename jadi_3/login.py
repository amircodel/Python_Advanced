import mysql.connector
import re
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
) 
def check(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):
        return True
    else:
        return False
user = input()
while check(user) == False:
    print('Right format of mail is expression@string.string , try again!')
    user = input()
password = input()
cursor = mydb.cursor()
sql = "INSERT INTO login (username, password) VALUES (%s, %s)"
val = (user,password)
cursor.execute(sql, val)
mydb.commit()