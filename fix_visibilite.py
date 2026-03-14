p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# 1. Grossir le bandeau flux imprevu
for i in range(len(lines)):
    if 'AJOUTER UN FLUX IMPREVU' in lines[i]:
        lines[i] = lines[i].replace('font-size:15px', 'font-size:24px')
        lines[i] = lines[i].replace('padding:8px 16px', 'padding:16px 24px')
        lines[i] = lines[i].replace('margin-bottom:12px', 'margin-bottom:20px')
        print(f'Bandeau grossi ligne {i+1}')
        break

# 2. Verifier bouton Annuler
annuler_present = False
for i in range(len(lines)):
    if 'undo_' in lines[i]:
        annuler_present = True
        print(f'Bouton Annuler present ligne {i+1}')
        break
if not annuler_present:
    print('Bouton Annuler ABSENT')

f=open(p,'w',encoding='utf-8')
f.writelines(lines)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
