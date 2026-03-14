p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Montrer les lignes 60-80
for j in range(58, 82):
    print(f'{j+1}: {lines[j].rstrip()[:120]}')
