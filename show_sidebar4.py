p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()
for j in range(2068, min(2120, len(lines))):
    print(f'{j+1}: {lines[j].rstrip()[:120]}')
