a = []
b = [1,a]
b[1].append(1)
print a, b

a = b =[]
b.append(1)
print a, b

a = []
b = []
b.append(1)
print a, b

a = []
b = [1,a]
a.append(b)
print a, b