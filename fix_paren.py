p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Ligne 25 : ajouter )
lines[24] = '    section[data-testid="stSidebar"] {display: block !important; opacity: 1 !important; width: 300px !important; transform: none !important;}\n'
lines[25] = '</style>""", unsafe_allow_html=True)\n'

f=open(p,'w',encoding='utf-8')
f.writelines(lines)
f.close()
print('Parenthese ajoutee')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
