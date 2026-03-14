p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Compter les sqlite3.connect restants
import re
matches = re.findall(r"sqlite3\.connect\(", t)
print(f'sqlite3.connect restants : {len(matches)}')

# Aussi chercher sq.connect (alias)
matches2 = re.findall(r"sq\.connect\(", t)
print(f'sq.connect restants : {len(matches2)}')

# Remplacer TOUS les sq.connect par db_wrapper.connect
t = t.replace("sq.connect(", "db_wrapper.connect(")
t = t.replace("sq.Row", "db_wrapper.Row")

# Remplacer TOUS les sqlite3.connect restants sauf dans les commentaires
lines = t.split('\n')
new_lines = []
for line in lines:
    if 'sqlite3.connect(' in line and '#' not in line.split('sqlite3')[0]:
        line = line.replace('sqlite3.connect(', 'db_wrapper.connect(')
    if 'sqlite3.Row' in line:
        line = line.replace('sqlite3.Row', 'db_wrapper.Row')
    new_lines.append(line)
t = '\n'.join(new_lines)

# Aussi remplacer import sqlite3 as sq
t = t.replace('import sqlite3 as sq', 'import db_wrapper as sq')

# Verifier combien il en reste
matches3 = re.findall(r"sqlite3\.connect\(", t)
matches4 = re.findall(r"sq\.connect\(", t)
print(f'Apres correction : sqlite3.connect={len(matches3)}, sq.connect={len(matches4)}')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
