p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Cacher le chevron natif qui ne marche pas
hide_native = '''
    /* Cacher le chevron natif non fonctionnel */
    button[data-testid="stBaseButton-headerNoPadding"] {
        display: none !important;
    }
    [data-testid="stSidebarCollapseButton"] {
        display: none !important;
    }
'''

# Ajouter dans le CSS du mode expanded
old = '''            section[data-testid="stSidebar"] {
                display: block !important; visibility: visible !important;
                transform: translateX(0) !important; width: 300px !important; min-width: 300px !important;
            }'''

new = '''            section[data-testid="stSidebar"] {
                display: block !important; visibility: visible !important;
                transform: translateX(0) !important; width: 300px !important; min-width: 300px !important;
            }''' + hide_native

t = t.replace(old, new)
print('Chevron natif cache')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
