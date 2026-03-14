p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()
for i in range(len(lines)):
    if 'sidebar' in lines[i]:
        print(f'{i+1}: {lines[i].rstrip()[:120]}')
