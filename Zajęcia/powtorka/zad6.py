liczby={'raz':3,'dwa':3,'trzy':4,'cztery':6}

[z for z in liczby.values()]     
    
[y for y in liczby.items()]     
    
"+".join(["%s" % v for k,v in liczby.items()])     
    
[x for x in liczby] 