p='C:/Users/BoulePiou/cockpit-raphael/db_wrapper.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

old = """DB_CONFIG = {
    'host': 'db.zyizvlrwsatxqehhqiwh.supabase.co',
    'port': 5432,
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'Seraphetraph/62//26**'
}"""

new = """import os
DB_CONFIG = {
    'host': os.environ.get('DB_HOST', 'db.zyizvlrwsatxqehhqiwh.supabase.co'),
    'port': int(os.environ.get('DB_PORT', 5432)),
    'dbname': os.environ.get('DB_NAME', 'postgres'),
    'user': os.environ.get('DB_USER', 'postgres'),
    'password': os.environ.get('DB_PASS', 'Seraphetraph/62//26**')
}"""

t = t.replace(old, new)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('db_wrapper mis a jour pour variables environnement')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
