def slownie(liczba):
    cyfry = {0:'zero', 1:'jeden', 2:'dwa', 3:'trzy', 
             4:'cztery', 5:'piec', 6:'szesc', 7:'siedem', 
             8:'osiem', 9:'dziewiec'}
    a = liczba
    wyn = []
    while a != 0:
        wyn =[(cyfry[a % 10])]+wyn
        a = a/10
    return wyn

print slownie(10234)

def slownie2(liczba):
    cyfry = ['zero','jeden','dwa','trzy','cztery','piec'
             'szesc','siedem','osiem','dziewiec']
    return map(lambda x:cyfry[int(x)],str(liczba))

print slownie2(10234)

a = 0xff

print a, hex(a), oct(a), bin(a)