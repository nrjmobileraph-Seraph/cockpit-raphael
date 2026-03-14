p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# 1. Supprimer les chemins Windows
import re
t = re.sub(r"db_wrapper\.connect\(['\"]C:.*?['\"]\)", "db_wrapper.connect()", t)
t = t.replace("backup_dir = 'C:/Users/BoulePiou/cockpit-raphael/backups'", "backup_dir = os.path.join(os.path.dirname(__file__), 'backups')")
t = t.replace("shutil.copy2('C:/Users/BoulePiou/cockpit-raphael/cockpit.db', bp)", "pass  # backup cloud")
t = t.replace("shutil.copy2(os.path.join(backup_dir, choix), 'C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "pass  # restore cloud")
print(f'BoulePiou apres: {t.count("BoulePiou")}')

# 2. Supprimer SEULEMENT les lignes CSS qui touchent stSidebar
lines = t.split('\n')
new_lines = []
for line in lines:
    if 'stSidebar' in line and ('display' in line or 'width' in line or 'transform' in line or 'opacity' in line or 'min-width' in line):
        print(f'  Supprime CSS: {line.strip()[:80]}')
        continue
    new_lines.append(line)
t = '\n'.join(new_lines)
print(f'stSidebar apres: {t.count("stSidebar")}')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
