from math import sqrt

a = float(raw_input("Podaj a: "))
b = float(raw_input("Podaj b: "))
c = float(raw_input("Podaj c: "))

# DELTA
delta = (b*b)-4*(a*c)
print delta

if delta < 0:
    print "Delta ujemna"
else:
    pd = sqrt(delta)
    
# pierwiastki    
if pd == 0:
    x = (-b)/(2*a)
    print x
else:
    # x1
    x1 = (-b-pd)/(2*a)
    print x1
    # x2
    x2 = (-b+pd)/(2*a)
    print x2