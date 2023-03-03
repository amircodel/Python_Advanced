import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
n = input()
if re.search(regex,n):
    print('OK')
else:
    print('WRONG')