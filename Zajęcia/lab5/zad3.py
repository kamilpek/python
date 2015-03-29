import math

class Punkt:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def dlug(self):
        return math.sqrt((self.__x*self.__x)+(self.__y*self.__y))   
    def __repr__(self):
        return '('+', '.join([str(self.__x), str(self.__y)])+')'
    def __getitem__(self, key):
        if key == "x":
            return self.__x
        elif key == "y":
            return self.__y
    def __setitem__(self, key, item):
        if key == "x":
            self.__x = item
        elif key == "y":
            self.__y = item
    def __cmp__(self, other):
        d1 = self.dlug()
        d2 = other.dlug()
        if d1 > d2:
            return -1
        elif d1 == d2:
            return 0
        else:
            return 1

p1 = Punkt(12,13)
p2 = Punkt(21,31)
l = [ p1, p2 ]
l.sort() 
l.sort(reverse=True)
print l
   
class Odcinek:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2
    def __repr__(self):
        return '['+', '.join([str(self.__p1), str(self.__p2)])+']'
    def __getitem__(self, key):
        if key == "p1":
            return self.__p1
        elif key == "p2":
            return self.__p2
        elif key == "x1":
            return self.__p1['x']
        elif key == "x2":
            return self.__p2['x']
        elif key == "y1":
            return self.__p1['y']
        elif key == "y2":
            return self.__p2['y']
    def __setitem__(self, key, item):
        if key == "p1":
            self.__p1 = item
        elif key == "p2":
            self.__p2 = item
        elif key == "x1":
            self.__p1['x'] = item
        elif key == "x2":
            self.__p2['x'] = item
        elif key == "y1":
            self.__p1['y'] = item
        elif key == "y2":
            self.__p2['y'] = item
     
 
ooo = Odcinek(Punkt(1,1), Punkt(2,2))

print ooo
print ooo['x1']
print ooo['p1']
ooo['p1'] = Punkt(3,3)
print ooo['p1']

   
# p = Punkt(1, 2)
# print p
#
# p['x'] = 9
# p['y'] = 10
#
# print p['x']
# print p['y']
#
# print p._Punkt__x

        