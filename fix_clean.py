p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

fixed=0
new_lines=[]
for i,l in enumerate(lines):
    # Reparer la ligne init_db cassee
    if 'def init_db()' in l and 'stException' in l:
        new_lines.append('def init_db():\n')
        fixed+=1
        continue
    # Supprimer toute ligne avec stException
    if 'stException' in l:
        fixed+=1
        continue
    new_lines.append(l)

f=open(p,'w',encoding='utf-8')
f.writelines(new_lines)
f.close()
print(f'Lignes corrigees: {fixed}')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
