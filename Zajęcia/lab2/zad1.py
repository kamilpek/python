from math import sqrt
from math import floor

x = int(raw_input("Podaj liczbe: "))

# way 1
jest = False
y = 1
while (y < x) and not jest:
    if (y * y) == x:
        jest = True
    y += 1
    
if jest:
    print 'TAK'
else:
    print 'NIE' 
    
# way 2
n = sqrt(x) 
print n.is_integer()

# way 3
if floor(n) == n:
    print 'tak'
else:
    print 'nie'