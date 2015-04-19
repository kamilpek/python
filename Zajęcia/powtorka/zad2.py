class A:

 i = 1

 def __init__(self, a):
     self.a = a

     self.__class__.i += 1

 def wypisz(self):

     print self.a, self.__class__.i

x = A(1)

y = A(2)

x.wypisz()

y.wypisz()