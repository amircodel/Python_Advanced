q = []
c = []
checker = []
n = input()
n = n.replace(",", ".")
l = n.split('.')
def intcon(handel):
    try:
        return int(handel)
    except:
        return 'na'
for i in l:
    if len(i) == 0:
        l.remove(i)
for i in l:
    for j in i.split():
        c.append(j)
        if i.split().index(j) == 0:
            continue
        else:
            if j == j.capitalize() and type(intcon(j)) != type(1):
                q.append(j)
            else:
                continue
qq = []
[qq.append(x) for x in q if x not in qq]
for i in range(len(c)):
    for j in qq:
        if j == c[i]:
            print('%i:%s'%(i+1,j))
            checker.append('%i:%s'%(i+1,j))
if checker == []:
    print('None')