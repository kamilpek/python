class Sum:
    def dodaj(self, x, y):
        print 'Brak implementacji'
    def __init__(self, start=[  ]):
        self.data = start
    def __dodaj__(self, other):
        return self.dodaj(self.data, other)
                          
class ListSum(Sum):             
    def dodaj(self, a, b):
        return a + b            # Konkatenacja / Dodawanie

class SlowSum(Sum):
    def dodaj(self, x, y):
        nowy = {  }
        for k in x.keys(  ): nowy[k] = x[k]
        for k in y.keys(  ): nowy[k] = y[k]
        return nowy
    
print ListSum().dodaj('maj', 'ster')
print ListSum().dodaj(128, 256)

a={1:1, 2:2, 3:3, 4:4, 5:5}
b={1:2, 2:3, 3:4, 4:5, 5:6}
print SlowSum().dodaj(a,b)