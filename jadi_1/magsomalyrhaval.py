list = []
counter= []
for i in range(10):
    num = int(input())
    list.append(num)
sorted(list)
def prime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False
def magaval(handel):
    global counter , c
    c = 0
    for i in range(handel + 1):
        try:
            d = handel % i
        except ZeroDivisionError:
            d = None
        if d == 0 and prime(i) == True :
            c += 1
    counter.append(c)
for l in list:
    magaval(l)
    if l == list.index(max(list)) and list.index(l) != counter.index(max(counter)):
        list[list.index(max(list))] = -1
print('%i %i'%(max(list),max(counter)))