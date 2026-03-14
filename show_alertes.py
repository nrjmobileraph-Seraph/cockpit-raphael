p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()
for i in range(len(lines)):
    if 'def calculer_alertes' in lines[i]:
        for j in range(i, min(i+30, len(lines))):
            print(f'{j+1}: {lines[j].rstrip()[:120]}')
        break
