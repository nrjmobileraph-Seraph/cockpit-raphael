p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Chercher les references au chemin Windows qui restent
for i, l in enumerate(lines):
    if 'BoulePiou' in l or 'cockpit.db' in l or 'C:/' in l or 'C:\\' in l:
        print(f'{i+1}: {l.strip()[:120]}')
