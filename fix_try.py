p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Trouver et supprimer le try mal place dans le sidebar
new_lines = []
for i, l in enumerate(lines):
    stripped = l.strip()
    # Supprimer le try isole qui casse le bloc
    if stripped == 'try:' and i > 2070 and i < 2090:
        print(f'Supprime try ligne {i+1}')
        continue
    if stripped == 'except:' and i > 2070 and i < 2100:
        print(f'Supprime except ligne {i+1}')
        continue
    if stripped == 'st.markdown("## Cockpit Raphael")' and i > 2070 and i < 2100:
        # Verifier si c est le doublon du except
        if i > 0 and 'except' in lines[i-1]:
            print(f'Supprime doublon ligne {i+1}')
            continue
    new_lines.append(l)

f=open(p,'w',encoding='utf-8')
f.writelines(new_lines)
f.close()
print('Try/except sidebar nettoye')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
