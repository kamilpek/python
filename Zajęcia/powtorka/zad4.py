def g(z, *a, **b):
    s = 0
    for k in b.keys():
        s = s + b[k]
    return s

print g(a = 3, z = 6, v = 9, w = 13) 