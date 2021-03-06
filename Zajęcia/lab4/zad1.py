osoby = [{'nazwisko':'Kowalski', 'waga':60, 'ulubione_dania':('schabowy', 'krupnik')}, 
         {'nazwisko':'Nowak', 'waga':80, 'ulubione_dania':('jajecznica', 'pomidorowa')}, 
         {'nazwisko':'Iksinski', 'waga':75, 'ulubione_dania':('chleb', 'barszcz')}, 
         {'nazwisko':'Nowakowski', 'waga':85, 'ulubione_dania':('ryz', 'bigos')}, 
         {'nazwisko':'Kowal', 'waga':75, 'ulubione_dania':('bulka', 'kebab')}, 
         {'nazwisko':'Smith', 'waga':95, 'ulubione_dania':('makaron', 'KFC')}, 
         {'nazwisko':'Wisniewski', 'waga':72, 'ulubione_dania':('zeberka', 'pizza')}, 
         {'nazwisko':'Dabrowski', 'waga':83, 'ulubione_dania':('pizza', 'tosty')}, 
         {'nazwisko':'Lewandowski', 'waga':68, 'ulubione_dania':('hot-dog', 'bigos')}, 
         {'nazwisko':'Wojcik', 'waga':76, 'ulubione_dania':('zupa', 'kaczka')}]

print osoby
print [o['nazwisko'] for o in osoby]

osoby.sort(key=lambda o:o['nazwisko'])
print [o['nazwisko'] for o in osoby]

osoby.sort(key=lambda o:o['waga'])
print [o['nazwisko'] for o in osoby]

osoby.sort(key=lambda o:o['ulubione_dania'][0], reverse=True)
print [o['nazwisko'] for o in osoby]

print sorted(osoby, key=lambda o:o['ulubione_dania'][0], reverse=True)

print sorted(osoby,
             cmp=lambda x,y: 1 if x<y else -1,
             key=lambda o:o['ulubione_dania'][0], reverse=True)

print [ o['nazwisko'] for o in sorted(osoby,
                                      cmp=lambda x,y: cmp(x[::-1],y[::-1]),
                                      key=lambda o:o['nazwisko']) ]