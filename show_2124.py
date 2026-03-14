p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Montrer les lignes 2120-2130 pour voir le bloc exact
for j in range(2118, 2132):
    print(f'{j+1}: {lines[j].rstrip()[:150]}')
