from collections import OrderedDict
from operator import itemgetter
qxnar = [0,0,0,0,0,0]
xanr = ['Horror', 'Romance', 'Comedy', 'History', 'Adventure', 'Action']
n = int(input())
for i in range(n):
    nxanr = []
    c = input()
    nx = c.split()
    nx.pop(0)
    for j in xanr:
        m = nx.count(j)
        nxanr.append(m)
    qxnar = [x+y for x,y in zip(qxnar,nxanr)]
q = OrderedDict(zip(xanr,qxnar))
q = sorted(q.items(), key= itemgetter(0),reverse=False)
for k,v in sorted(q, key= itemgetter(1),reverse=True):
    print('%s : %i'%(k,v))