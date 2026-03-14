p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Montrer autour de 2100
for j in range(2096, 2106):
    print(f'{j+1}: {repr(lines[j].rstrip()[:100])}')
