import pandas as pd
import re
print('-------------------------------------------------\n')
df = pd.read_excel(r'a.xlsx')
print('-------------------------------------------------\n')
code_col = []
for col in df.columns:
    if re.search(r'کد ملی', col) or re.search(r'کدملی', col):
        code_col.append(col)
code_meli = df.loc[:,code_col]
def meli(c):
    o = str(c)
    if len(o) < 10:
        while len(o) <  10:
            o = '0' + o
    return o
for header in code_col:
    lstcode = []
    lstcode.extend((df[header].values[:]))
    for code in lstcode:
        print(meli(code))
        df.at[header,code]= meli(code)
print('-------------------------------------------------\n')
print(code_meli)