p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Compter les remplacements
n=0

# SCI : ancien 291 800 ou 290 842 -> 296 100
for old in ['291 800','291800','290 842','290842']:
    if old in t:
        t=t.replace(old,'296 100')
        n+=1
        print(f'Remplace {old} -> 296 100')

# Capital : ancien 475 000 ou 477 000 ou 468 192 -> 461 000
for old in ['475 000','475000','477 000','477000','468 192','468192']:
    if old in t:
        t=t.replace(old,'461 000')
        n+=1
        print(f'Remplace {old} -> 461 000')

# Total cash : ancien 509 200 ou 502 392 -> 513 500
for old in ['509 200','509200','502 392','502392']:
    if old in t:
        t=t.replace(old,'513 500')
        n+=1
        print(f'Remplace {old} -> 513 500')

# Patrimoine total : ancien 680 000 ou 673 192 ou 694 000 -> 680 000
for old in ['673 192','673192','694 000','694000']:
    if old in t:
        t=t.replace(old,'680 000')
        n+=1
        print(f'Remplace {old} -> 680 000')

# Loyer net : ancien 448 -> 320
if '448' in t:
    t=t.replace('448','320')
    n+=1
    print('Remplace 448 -> 320')

# Appart valeur : 183 000 -> 199 000
for old in ['183 000','183000']:
    if old in t:
        t=t.replace(old,'199 000')
        n+=1
        print(f'Remplace {old} -> 199 000')

# Garage : 22 000 -> 20 000
# Attention pas remplacer partout, seulement dans contexte garage
# On le fera manuellement si besoin

# Version
t=t.replace('v4.1','v4.3')
t=t.replace('v4.2','v4.3')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print(f'Total: {n} remplacements')
print('Patch chiffres v4.3 OK')
