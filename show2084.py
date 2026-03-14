p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()
for j in range(2078, 2095):
    print(f'{j+1}: {repr(lines[j][:100])}')
