class Sum:
    def dodaj(self, x, y):
        print 'Brak implementacji'
    def __init__(self, start=[  ]):
        self.data = start
    def __dodaj__(self, other):
        return self.dodaj(self.data, other)
                          
class ListSum(Sum):
    def dodaj(self, a, b):
        return a + b

class SlowSum(Sum):
    def dodaj(self, x, y):
        nowy = {  }
        for k in x.keys(  ): nowy[k] = x[k]
        for k in y.keys(  ): nowy[k] = y[k]
        return nowy
    
# x = int(raw_input("Podaj x "))
# y = int(raw_input("Podaj y ")) 
ListSum().dodaj(1, 2, 3)