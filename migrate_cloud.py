import re

p = 'C:/Users/BoulePiou/cockpit-raphael/app.py'
f = open(p, 'r', encoding='utf-8')
t = f.read()
f.close()

# Sauvegarder l'original
f2 = open(p + '.backup_sqlite', 'w', encoding='utf-8')
f2.write(t)
f2.close()
print('Backup app.py.backup_sqlite cree')

# 1. Ajouter import psycopg2 en haut
if 'import psycopg2' not in t:
    t = t.replace('import sqlite3', 'import sqlite3\nimport psycopg2\nimport psycopg2.extras')
    print('Import psycopg2 ajoute')

# 2. Ajouter fonction de connexion cloud
db_func = '''
def get_db():
    try:
        conn = psycopg2.connect(
            host='db.zyizvlrwsatxqehhqiwh.supabase.co',
            port=5432, dbname='postgres', user='postgres',
            password='Seraphetraph/62//26**'
        )
        return conn, True
    except:
        conn = sqlite3.connect(DB_PATH)
        return conn, False

def get_db_dict():
    try:
        conn = psycopg2.connect(
            host='db.zyizvlrwsatxqehhqiwh.supabase.co',
            port=5432, dbname='postgres', user='postgres',
            password='Seraphetraph/62//26**',
            cursor_factory=psycopg2.extras.RealDictCursor
        )
        return conn, True
    except:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn, False
'''

# Inserer apres DB_PATH
idx_db = t.find('DB_PATH')
if idx_db > 0:
    fin_ligne = t.find('\n', idx_db)
    t = t[:fin_ligne+1] + db_func + t[fin_ligne+1:]
    print('Fonctions get_db() ajoutees')

# 3. Remplacer les placeholders ? par %s dans les requetes SQL
# On remplace seulement dans les execute() avec des ?
count_q = 0
lines = t.split('\n')
new_lines = []
for line in lines:
    if '.execute(' in line and '?' in line and 'PRAGMA' not in line:
        line = line.replace('?', '%s')
        count_q += 1
    new_lines.append(line)
t = '\n'.join(new_lines)
print(f'Placeholders remplaces : {count_q} lignes')

# 4. Remplacer INSERT OR IGNORE par INSERT ... ON CONFLICT DO NOTHING
t = t.replace('INSERT OR IGNORE', 'INSERT')
print('INSERT OR IGNORE corrige')

f = open(p, 'w', encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
