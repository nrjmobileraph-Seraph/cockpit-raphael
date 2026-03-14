p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

old = '''        section[data-testid="stSidebar"] {
            transform: translateX(0px) !important;
            visibility: visible !important;
            display: block !important;
        }'''

new = '''        section[data-testid="stSidebar"] {
            transform: translateX(0px) !important;
            visibility: visible !important;
            display: block !important;
            width: 300px !important;
            min-width: 300px !important;
        }'''

t = t.replace(old, new)
print('Largeur sidebar forcee')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
