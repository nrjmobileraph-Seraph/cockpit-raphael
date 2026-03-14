with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Remplacer TOUTES les connexions avec chemin
code = code.replace("sqd.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "db_wrapper.connect()")
code = code.replace("sq2.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "db_wrapper.connect()")
code = code.replace("db_wrapper.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "db_wrapper.connect()")

# Supprimer les import sqlite3 locaux
code = code.replace("    import sqlite3 as sqd\n", "")
code = code.replace("        import sqlite3 as sq2\n", "")

# Remplacer sqd et sq2 par db_wrapper dans les noms de variables
code = code.replace("dbd = sqd.", "dbd = db_wrapper.")
code = code.replace("db4 = sqd.", "db4 = db_wrapper.")
code = code.replace("db5 = sqd.", "db5 = db_wrapper.")
code = code.replace("db3 = sq2.", "db3 = db_wrapper.")

# Supprimer le shutil.copy2 avec BoulePiou
code = code.replace("                shutil.copy2(os.path.join(backup_dir, choix), 'C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "                pass")

# Ligne 1829 import sqlite3 dans boursobank
code = code.replace("    import sqlite3, urllib.parse", "    import urllib.parse")

with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'w', encoding='utf-8') as f:
    f.write(code)

import ast
ast.parse(code)
print(f'ast.parse : PASS')
print(f'sqlite3 : {code.count("sqlite3")}')
print(f'BoulePiou : {code.count("BoulePiou")}')
print(f'db_wrapper.connect() : {code.count("db_wrapper.connect()")}')
print(f'Pages : {code.count("def page_")}')
print('SUCCES')
