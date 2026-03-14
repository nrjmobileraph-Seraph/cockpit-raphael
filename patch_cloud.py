p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Sauvegarder
f2=open(p+'.backup_local','w',encoding='utf-8')
f2.write(t)
f2.close()
print('Backup cree')

# 1. Ajouter import db_wrapper apres import sqlite3
t = t.replace('import sqlite3\n', 'import sqlite3\nimport db_wrapper\n', 1)
print('Import db_wrapper ajoute')

# 2. Remplacer tous les sqlite3.connect(...) par db_wrapper.connect()
# Sauf dans init_db (backup) et dans les scripts de test
import re
count = 0
lines = t.split('\n')
new_lines = []
for line in lines:
    if 'sqlite3.connect(' in line and 'shutil' not in line and 'backup' not in line.lower():
        line = line.replace('sqlite3.connect(', 'db_wrapper.connect(')
        count += 1
    if 'sqlite3.Row' in line:
        line = line.replace('sqlite3.Row', 'db_wrapper.Row')
    new_lines.append(line)
t = '\n'.join(new_lines)
print(f'Connexions remplacees : {count}')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
