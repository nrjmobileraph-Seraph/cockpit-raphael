p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()
for i in range(2220, 2230):
    print(f'{i+1}: {lines[i].rstrip()[:120]}')
