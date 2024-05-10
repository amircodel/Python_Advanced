from operator import itemgetter
wiran = []
wspain = []
wportugal = []
wmorocoo = []
siran = []
sspain = []
sportugal = []
smorocoo = []
piran = []
pspain = []
pportugal = []
pmorocoo = []
def wld(teama,z):
    if z == 1 :
        if gold(result,1) > 0 :
            return 1
        elif gold(result,1) < 0 :
            return -1
        else:
            return 0
    else:
        if gold(result,2) > 0 :
            return 1
        elif gold(result,2) < 0 :
            return -1
        else:
            return 0
def gold(teamb,z):
    if z == 1:
        return teamb[0] - teamb[1]
    else:
        return teamb[1] - teamb[0]
def point(teamc,z):
    if z == 1:
        if wld(result,1) == 1:
            return 3
        elif wld(result,1) == -1:
            return 0
        else:
            return 1
    else:
        if wld(result,2) == 1:
            return 3
        elif wld(result,2) == -1:
            return 0
        else:
            return 1
r = input()
result = r.split('-')
for i in result:
    result[result.index(i)] = int(i)
wiran.append(wld(result,1))
wspain.append(wld(result,2))
siran.append(gold(result,1))
sspain.append(gold(result,2))
piran.append(point(result,1))
pspain.append(point(result,2))
r = input()
result = r.split('-')
for i in result:
    result[result.index(i)] = int(i)
wiran.append(wld(result,1))
wportugal.append(wld(result,2))
siran.append(gold(result,1))
sportugal.append(gold(result,2))
piran.append(point(result,1))
pportugal.append(point(result,2))
r = input()
result = r.split('-')
for i in result:
    result[result.index(i)] = int(i)
wiran.append(wld(result,1))
wmorocoo.append(wld(result,2))
siran.append(gold(result,1))
smorocoo.append(gold(result,2))
piran.append(point(result,1))
pmorocoo.append(point(result,2))
r = input()
result = r.split('-')
for i in result:
    result[result.index(i)] = int(i)
wspain.append(wld(result,1))
wportugal.append(wld(result,2))
sspain.append(gold(result,1))
sportugal.append(gold(result,2))
pspain.append(point(result,1))
pportugal.append(point(result,2))
r = input()
result = r.split('-')
for i in result:
    result[result.index(i)] = int(i)
wspain.append(wld(result,1))
wmorocoo.append(wld(result,2))
sspain.append(gold(result,1))
smorocoo.append(gold(result,2))
pspain.append(point(result,1))
pmorocoo.append(point(result,2))
r = input()
result = r.split('-')
for i in result:
    result[result.index(i)] = int(i)
wportugal.append(wld(result,1))
wmorocoo.append(wld(result,2))
sportugal.append(gold(result,1))
smorocoo.append(gold(result,2))
pportugal.append(point(result,1))
pmorocoo.append(point(result,2))
liran = wiran.count(-1)
lspain = wspain.count(-1)
lportugal = wportugal.count(-1)
lmorocoo = wmorocoo.count(-1)
diran = wiran.count(0)
dspain = wspain.count(0)
dportugal = wportugal.count(0)
dmorocoo = wmorocoo.count(0)
wiran = wiran.count(1)
wspain = wspain.count(1)
wportugal = wportugal.count(1)
wmorocoo = wmorocoo.count(1)
siran = sum(siran)
piran = sum(piran)
sspain = sum(sspain)
pspain = sum(pspain)
sportugal = sum(sportugal)
pportugal = sum(pportugal)
smorocoo = sum(smorocoo)
pmorocoo = sum(pmorocoo)
iran= ['Iran',wiran,liran,diran,siran,piran]
spain= ['Spain',wspain,lspain,dspain,sspain,pspain]
portugal= ['Portugal',wportugal,lportugal,dportugal,sportugal,pportugal]
morocoo= ['Morocco',wmorocoo,lmorocoo,dmorocoo,smorocoo,pmorocoo]
j= [iran,morocoo,portugal,spain]
j = sorted(j, key=itemgetter(5,1), reverse=True)
for o in j:
    o = tuple(o)
    print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i'%o)