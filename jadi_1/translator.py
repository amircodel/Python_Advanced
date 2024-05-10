from collections import OrderedDict
q = OrderedDict()
n = int(input())
for i in range(n):
    l = []
    m = input()
    l = m.split()
    q[l[0]]= l[1:4]
d = input().split()
for sh in d:
    for k,v in q.items():
            for j in q.get(k):
                if sh == j:
                    key_list = list(q.keys())
                    val_list = list(q.values())
                    position = val_list.index(q.get(k))
                    d[d.index(sh)] = key_list[position]
print(' '.join(d))