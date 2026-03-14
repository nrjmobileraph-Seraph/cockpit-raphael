p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# 1. Verifier si le flux imprevu est present
if 'flux impреvu' in t or 'flux imprevu' in t:
    print('Flux imprevu deja present')
else:
    print('Flux imprevu ABSENT - il faut le reinstaller')

# 2. Verifier le CSS cache erreurs
if 'stException' in t:
    print('CSS stException present')
else:
    print('CSS stException ABSENT')

# 3. Compter les pages
pages = ['page_dashboard', 'page_jalons', 'page_suivi_av', 'page_lmnp', 'page_caf_pch', 'page_annexe']
for p2 in pages:
    print(f'{p2}: {"OUI" if "def "+p2 in t else "NON"}')
