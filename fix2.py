with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Supprimer les lignes row_factory
    if 'row_factory' in line:
        continue
    # Remplacer les connexions sqlite restantes
    if 'sq.connect' in line:
        line = line.replace("sq.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "db_wrapper.connect()")
        line = line.replace('sq.connect("C:/Users/BoulePiou/cockpit-raphael/cockpit.db")', 'db_wrapper.connect()')
    if 'sqlite3.connect' in line:
        line = line.replace("sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "db_wrapper.connect()")
    # Supprimer import sq
    if 'import sqlite3 as sq' in line:
        continue
    if line.strip() == 'import sqlite3':
        continue
    # Nettoyer db_j = sq. -> db_j = db_wrapper
    line = line.replace('db_j = sq.Row', '# row removed')
    new_lines.append(line)

with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

import ast
with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    code = f.read()
ast.parse(code)
print(f'ast.parse : PASS')
print(f'sqlite3 restants : {code.count("sqlite3")}')
print(f'sq.connect restants : {code.count("sq.connect")}')
print(f'BoulePiou restants : {code.count("BoulePiou")}')
print(f'Pages : {code.count("def page_")}')
print('SUCCES')
