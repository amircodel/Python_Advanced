import mysql.connector
import csv
main = []
mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="",
  database="python"
)
cursor = mydb.cursor()
cursor.execute("SELECT Area, COUNT(Area) FROM `melkehtabriz` GROUP BY Area ORDER BY COUNT(Area) DESC;")
with open('report.csv', 'w+', encoding='UTF8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['منطقه','تعداد آگهی'])
    for area, count in cursor:
        writer.writerow([area,count])