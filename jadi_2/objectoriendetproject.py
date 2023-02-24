from random import choice
list = ['حسین','مازیار','اکبر','نیما','مهدی','فرهاد','محمد','خشایار','میلاد','مصطفی','امین','سعید','پویا','پوریا','رضا','علی','بهزاد','سهیل','بهروز','شهروز','سامان','محسن']
class Human():
    def __init__(self,name):
        self.name = name
class Player(Human):
    groups = ['A','A','A','A','A','A','A','A','A','A','A','B','B','B','B','B','B','B','B','B','B','B']
    def __init__(self,n):
        self.n = n
    def draw(self):
        self.n = choice(self.groups)
        print('%s %s' %(i,self.n))
        self.groups.remove(self.n)
for i in list:
    info = Player(i)
    info.draw()
