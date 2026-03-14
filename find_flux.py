p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Trouver les lignes avec "FLUX IMPREVU" et "Cliquer ici"
for i, l in enumerate(lines):
    if 'FLUX IMPREVU' in l or 'flux imprevu' in l.lower() or 'Cliquer ici pour saisir' in l:
        print(f'Ligne {i+1}: {l.strip()[:80]}')
