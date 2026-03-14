p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Supprimer les imports mal places (lignes 537-538)
new_lines = []
skip_next = False
for i, l in enumerate(lines):
    # Supprimer les imports psycopg2 qui sont indentes incorrectement
    stripped = l.strip()
    if stripped == 'import psycopg2' and i > 10:
        print(f'Supprime import mal place ligne {i+1}')
        continue
    if stripped == 'import psycopg2.extras' and i > 10:
        print(f'Supprime import mal place ligne {i+1}')
        continue
    if stripped.startswith('import psycopg2.extras as') and i > 10:
        print(f'Supprime import mal place ligne {i+1}')
        continue
    new_lines.append(l)

# Aussi corriger le sq.connect et sq.Row qui viennent de l'alias
t = ''.join(new_lines)
# Remettre sqlite3 la ou sq a ete mis par erreur
t = t.replace('sq.connect(', 'sqlite3.connect(')
t = t.replace('sq.Row', 'sqlite3.Row')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Imports mal places supprimes')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
