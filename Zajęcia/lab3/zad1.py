# Algorytm Euklidesa
# Autor: Kamil Pek

a = int(raw_input("Podaj liczbe: "))
b = int(raw_input("Podaj liczbe: "))

def euklides(a, b):
    while b:
        a, b = b, a%b
    return a

c=euklides(a, b)

print 'NWD: ', c