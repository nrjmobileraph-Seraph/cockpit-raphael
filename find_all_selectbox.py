p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()
print(f'Fichier : {len(lines)} lignes')
print()
print('=== TOUTES LES LIGNES SELECTBOX ===')
for i, line in enumerate(lines):
    if 'selectbox' in line.lower():
        print(f'Ligne {i+1}: {line.rstrip()[:150]}')
        if i > 0: print(f'  avant {i}: {lines[i-1].rstrip()[:150]}')
        if i < len(lines)-1: print(f'  apres {i+2}: {lines[i+1].rstrip()[:150]}')
        print('---')
