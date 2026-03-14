p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Chercher TOUTES les references a sqlite3 ou sq. qui posent probleme
import re
lines = t.split('\n')
for i, l in enumerate(lines):
    if 'sq.' in l and 'db_wrapper' not in l and '#' not in l.split('sq.')[0] and 'mask' not in l:
        print(f'Ligne {i+1}: {l.strip()[:100]}')
    if 'sqlite3' in l and 'import' not in l and '#' not in l.split('sqlite3')[0]:
        print(f'Ligne {i+1}: {l.strip()[:100]}')
