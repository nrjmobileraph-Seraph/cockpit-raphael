p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

old = '''def init_db():
    import shutil, os
    if not os.path.exists(DB_PATH):
        return
    try:
        backup_dir = os.path.join(os.path.dirname(DB_PATH), 'backups')
    os.makedirs(backup_dir, exist_ok=True)
    from datetime import date as _d
    bp = os.path.join(backup_dir, f'cockpit_{_d.today()}.db')
    if not os.path.exists(bp):
        try:
            shutil.copy2(DB_PATH, bp)
            backups = sorted(os.listdir(backup_dir))
            while len(backups) > 10:
                os.remove(os.path.join(backup_dir, backups.pop(0)))
        except:
            pass'''

new = '''def init_db():
    import shutil, os
    try:
        backup_dir = os.path.join(os.path.dirname(DB_PATH), 'backups')
        os.makedirs(backup_dir, exist_ok=True)
        from datetime import date as _d
        bp = os.path.join(backup_dir, f'cockpit_{_d.today()}.db')
        if not os.path.exists(bp) and os.path.exists(DB_PATH):
            shutil.copy2(DB_PATH, bp)
            backups = sorted(os.listdir(backup_dir))
            while len(backups) > 10:
                os.remove(os.path.join(backup_dir, backups.pop(0)))
    except:
        pass'''

t = t.replace(old, new)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('init_db corrige')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
