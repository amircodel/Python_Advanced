from collections import OrderedDict
from operator import itemgetter
qxnar = [0,0,0,0,0,0]
xanr = ['Horror', 'Romance', 'Comedy', 'History', 'Adventure', 'Action']
n = int(input())
for i in range(n):
    c = input()
    nx = c.split()
    nx.pop(0)
    for j in xanr:
        nxanr = []
        m = nx.count(j)
        nxanr.append(m)
    for o in range(6):
        for k in nxanr:
            pass
        print(k)
        # qxnar[o] += k
q = OrderedDict(zip(xanr,qxnar))
for k,v in sorted(q.items(), key= itemgetter(1,0)):
    print('%s : %i'%(k,v))
