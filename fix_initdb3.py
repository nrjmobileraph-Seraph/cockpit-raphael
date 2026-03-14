p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver init_db et wrapper TOUT le contenu dans try/except
# Trouver le debut et la fin
lines = t.split(chr(10))
start = -1
end = -1
for i, l in enumerate(lines):
    if 'def init_db():' in l:
        start = i
    if start >= 0 and i > start and l != '' and not l.startswith(' ') and not l.startswith(chr(9)):
        end = i
        break

if start >= 0 and end > start:
    # Remplacer init_db par une version safe
    old_func = chr(10).join(lines[start:end])
    new_func = '''def init_db():
    try:
        import shutil, os
        backup_dir = os.path.join(os.path.dirname(DB_PATH), 'backups')
        os.makedirs(backup_dir, exist_ok=True)
        from datetime import date as _d
        bp = os.path.join(backup_dir, f'cockpit_{_d.today()}.db')
        if not os.path.exists(bp) and os.path.exists(DB_PATH):
            shutil.copy2(DB_PATH, bp)
    except:
        pass'''
    t = t.replace(old_func, new_func)
    print(f'init_db remplace (lignes {start+1}-{end})')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
