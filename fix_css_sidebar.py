p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Supprimer le CSS qui force le sidebar ouvert
t = t.replace('    [data-testid="stSidebar"] {display: block !important; width: 300px !important; min-width: 300px !important;}', '')
t = t.replace('    [data-testid="stSidebar"] > div {display: block !important; width: 300px !important;}', '')
t = t.replace('    section[data-testid="stSidebar"] {display: block !important; opacity: 1 !important; width: 300px !important; transform: none !important;}', '')

print('CSS force supprime')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
