import datetime
n = input()
year, month, day = map(int, n.split('/'))
try:
    d = datetime.date(year, month, day)
    todayyear = datetime.date.today().year
    print(datetime.date.today().year - year - ((datetime.date.today().month, datetime.date.today().day) < (month,day)))
except ValueError:
    print('WRONG')