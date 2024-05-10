lst = []
counter= []
for i in range(10):
    num = int(input())
    lst.append(num)
lst = sorted(lst, reverse= True)
def prime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False
def magavall(handel,z):
    global counter
    c = 0
    for i in range(handel + 1):
        try:
            d = handel % i
        except ZeroDivisionError:
            d = None
        if d == 0 and prime(i) == True :
            c += 1
    if z == 0 :
        counter.append(c)
    else:
        return c
for l in lst:
    magavall(l,0)
for k in lst:
    if magavall(k,1) == max(counter):
        if k == max(lst):
            print("%i %i" %(k,max(counter)))
            break
    else:
        lst[lst.index(k)] = -1