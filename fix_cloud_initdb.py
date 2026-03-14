p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Wrapper le backup dans un try/except plus solide
old = "    import shutil, os\n    backup_dir = os.path.join(os.path.dirname(DB_PATH), 'backups')"
new = "    import shutil, os\n    try:\n        backup_dir = os.path.join(os.path.dirname(DB_PATH), 'backups')"

t = t.replace(old, new)

# Fermer le try/except avant le reste de init_db
old2 = "        except:\n            pass"
# Trouver le bon except dans init_db
# On va plutot wrapper tout init_db backup dans un gros try
# Approche plus simple : chercher la fin du bloc backup
t = t.replace("            pass\ndef init_db():", "            pass\n    except:\n        pass\ndef init_db():")

# En fait, approche plus directe : ajouter un check si DB_PATH existe
old_backup = "    import shutil, os\n    try:\n        backup_dir"
new_backup = "    import shutil, os\n    if not os.path.exists(DB_PATH):\n        return\n    try:\n        backup_dir"

t = t.replace(old_backup, new_backup)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('init_db protege pour le cloud')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
