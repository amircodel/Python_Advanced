import mysql.connector
from operator import itemgetter
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test2"
)
cursor = mydb.cursor()
cursor.execute("SELECT * FROM worker")
res = cursor.fetchall()
res = sorted(res,key= itemgetter(1),reverse=False)
for i in sorted(res,key= itemgetter(2),reverse=True):
    print('%s %d %d'%(i[0],i[2],i[1]))