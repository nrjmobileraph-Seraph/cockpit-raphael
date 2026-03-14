p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Supprimer la ligne stException mal placee
new_lines = [l for l in lines if 'stException' not in l]
removed = len(lines) - len(new_lines)
print(f'Lignes stException supprimees: {removed}')

# Trouver main() et ajouter le CSS apres init_db()
for i in range(len(new_lines)):
    if 'init_db()' in new_lines[i] and 'def ' not in new_lines[i]:
        new_lines.insert(i+1, '    st.markdown("<style>.stException{display:none !important}</style>", unsafe_allow_html=True)\n')
        print(f'CSS ajoute apres ligne {i+1}')
        break

f=open(p,'w',encoding='utf-8')
f.writelines(new_lines)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
