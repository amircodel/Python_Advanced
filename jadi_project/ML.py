import mysql.connector
from sklearn import tree
# Get data
mydb = mysql.connector.connect(
  host="localhost",
  port="3307",
  user="root",
  password="",
  database="python"
)
def ordstr(demo):
    o = ''
    for i in demo:
        o = o + str(ord(i))
    if int(o) > 3*(10**37):
        return int(o[0:37])
    return int(o)
main = []
cursor = mydb.cursor()
query = "SELECT Area, Meterage, PPM, Floor, Rooms, Allfloors, HPF, old, Situation, TypeBuilding FROM `melkehtabriz`"
cursor.execute(query)
for Area, Meterage, PPM, Floor, Rooms, Allfloors, HPF, old, Situation, TypeBuilding in cursor:
    data = [ordstr(Area), Meterage, PPM, ordstr(Floor), Rooms, Allfloors, HPF, old, ordstr(Situation), ordstr(TypeBuilding)]
    main.append(data)
# ML
x = []
y = []
for lst in main:
    y.append(lst.pop(2))
    x.append(lst)
yourArea = ordstr(input("Enter Area:"))
yourMeterage = float(input("Enter Meterage:"))
yourFloor = ordstr(input("Enter floor of your home:"))
yourRooms = int(input("Enter how many Rooms has:"))
yourAllfloors= int(input("Enter how many floor of the buliding has:"))
yourHPF = int(input("Enter how many homes per a floor of the building has:"))
yourold = int(input("Enter built year:"))
yourSituation = ordstr(input("Enter situation of the home:"))
yourTypeBuilding = ordstr(input("Enter type of building:"))
yours = [[yourArea,yourMeterage,yourFloor,yourRooms,yourAllfloors,yourHPF,yourold,yourSituation,yourTypeBuilding]]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
answer = clf.predict(yours)
print('It looks like your house is worth {:,} Toman per meter and is worth {:,} Toman in total'.format(answer[0],int(answer[0]*yourMeterage)))