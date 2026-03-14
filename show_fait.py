p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()
for i in range(1278, 1300):
    print(f'{i+1}: {lines[i].rstrip()[:120]}')
