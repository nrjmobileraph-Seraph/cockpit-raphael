p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Remplacer TOUS les chemins Windows dans les connect()
t = t.replace("db_wrapper.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "db_wrapper.connect()")
t = t.replace('db_wrapper.connect("C:/Users/BoulePiou/cockpit-raphael/cockpit.db")', 'db_wrapper.connect()')
t = t.replace("db_wrapper.connect(DB_PATH)", "db_wrapper.connect()")

# Aussi le row_factory qui sert a rien avec db_wrapper
t = t.replace("db_j.row_factory = db_wrapper.Row", "# row_factory geree par db_wrapper")

print(f'Chemins Windows supprimes')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
