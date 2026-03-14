p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()
print(f'Ligne 2085: {lines[2084].rstrip()[:200]}')
print(f'Ligne 2086: {lines[2085].rstrip()[:200]}')
