n= int(input())
old= input()
old = old.split()
old = [int(i) for i in old]
height = input()
height = height.split()
height = [int(i) for i in height]
weight = input()
weight = weight.split()
weight = [int(i) for i in weight]
class Students():
    def __init__(self, n, old, weight, height):
        self.old = old
        self.weight = weight
        self.height = height
        self.n = n
    def avg_old(self):
        return sum(self.old)/self.n
    def avg_height(self):
        return sum(self.height)/self.n
    def avg_weight(self):
        return sum(self.weight)/self.n
A = Students(n, old, weight, height)
A_avg_old = A.avg_old()
A_avg_height = A.avg_height()
A_avg_weight = A.avg_weight()
n= int(input())
old= input()
old = old.split()
old = [int(i) for i in old]
height = input()
height = height.split()
height = [int(i) for i in height]
weight = input()
weight = weight.split()
weight = [int(i) for i in weight]
B = Students(n, old, weight, height)
B_avg_old = B.avg_old()
B_avg_height = B.avg_height()
B_avg_weight = B.avg_weight()
def winner():
    if A_avg_height > B_avg_height :
        return 'A'
    elif A_avg_height < B_avg_height :
        return 'B'
    else:
        if A_avg_weight < B_avg_weight :
            return 'A'
        elif A_avg_weight > B_avg_weight :
            return 'B'
        else:
            return 'Same'
list = [A_avg_old,A_avg_height,A_avg_weight,B_avg_old,B_avg_height,B_avg_weight,winner()]
for i in list :
    print(i)