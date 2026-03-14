p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Remplacer tous les sqd.connect et sq2.connect avec chemin Windows
t = t.replace("sqd.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "db_wrapper.connect()")
t = t.replace("sq2.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "db_wrapper.connect()")

# Remplacer import sqlite3 as sqd et sq2
t = t.replace("import sqlite3 as sqd", "import db_wrapper as sqd")
t = t.replace("import sqlite3 as sq2", "import db_wrapper as sq2")

# Aussi remplacer sqd.Row et sq2.Row
t = t.replace("sqd.Row", "db_wrapper.Row")
t = t.replace("sq2.Row", "db_wrapper.Row")

# Wrapper les backups dans try/except pour le cloud
t = t.replace("backup_dir = 'C:/Users/BoulePiou/cockpit-raphael/backups'", "backup_dir = os.path.join(os.path.dirname(__file__), 'backups')")
t = t.replace("shutil.copy2('C:/Users/BoulePiou/cockpit-raphael/cockpit.db', bp)", "pass  # backup local desactive sur cloud")
t = t.replace("shutil.copy2(os.path.join(backup_dir, choix), 'C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "pass  # restore local desactive sur cloud")

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Tous les chemins Windows corriges')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
