from operator import itemgetter
q = []
n = int(input())
for i in range(n):
    al = []
    a = input()
    al = a.split('.')
    al[0] = al[0].lower()
    al[1] = al[1].capitalize()
    q.append(al)
for i,j,k in sorted(q, key= itemgetter(0,1), reverse=False):
    print(i,j,k)