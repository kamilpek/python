a = 1
b = 2
c = 2

print (a>b and [a] or [b])[0]

print a if a>b else b

x =((a==0) and [
                (c == 0 and ['duzo'] or ['nie ma'])[0]
                ] or [-c/float(a)]
    )[0]
    
print x