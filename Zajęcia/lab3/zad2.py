# Iloczyn skalarny wedlug dlugosci wektora i cosinusa kata
# Autor: Kamil Pek

from math import cos
from math import radians

a = int(raw_input("Podaj dlugosc wektora a: "))
b = int(raw_input("Podaj dlugosc wektora b: "))
c = int(raw_input("Podaj kat zawarty miedzy wektorami: "))

rad = radians(c)
kosinus = cos(rad)

if c==90:
    print 'Iloczyn skalarny dwoch wektorow jest rowny 0.'
else:
    def iloczyn(a,b,c):
        return a*b*kosinus
    i = iloczyn(a,b,c)
    print 'Iloczyn skalarny wektorow jest rowny: ', i