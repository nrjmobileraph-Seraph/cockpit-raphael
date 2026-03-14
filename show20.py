p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()
for j in range(14, 28):
    print(f'{j+1}: {repr(lines[j].rstrip()[:120])}')
