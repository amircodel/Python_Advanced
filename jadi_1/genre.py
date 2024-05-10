from collections import OrderedDict
from operator import itemgetter
q_genre = [0,0,0,0,0,0]
genre = ['Horror', 'Romance', 'Comedy', 'History', 'Adventure', 'Action']
n = int(input())
for i in range(n):
    nxanr = []
    c = input()
    nx = c.split()
    nx.pop(0)
    for j in genre:
        m = nx.count(j)
        nxanr.append(m)
    q_genre = [x+y for x,y in zip(q_genre,nxanr)]
q = OrderedDict(zip(genre,q_genre))
q = sorted(q.items(), key= itemgetter(0),reverse=False)
for k,v in sorted(q, key= itemgetter(1),reverse=True):
    print('%s : %i'%(k,v))