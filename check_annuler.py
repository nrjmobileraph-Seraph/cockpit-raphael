p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
lines=t.split(chr(10))
for i, l in enumerate(lines):
    if 'DEJA FAIT' in l or 'undo_' in l or 'Annuler' in l:
        print(f'{i+1}: {l.strip()[:100]}')
