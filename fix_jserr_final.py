p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# 1. Ajouter CSS pour cacher erreurs JS - dans le tout premier st.set_page_config ou juste apres les imports
# Trouver st.set_page_config
idx = t.find('st.set_page_config')
if idx > 0:
    # Trouver la fin de cette ligne
    fin = t.find(chr(10), idx)
    # Ajouter le CSS juste apres
    css_hide = chr(10) + 'st.markdown("<style>div[data-testid=stException]{display:none !important}</style>", unsafe_allow_html=True)' + chr(10)
    t = t[:fin+1] + css_hide + t[fin+1:]
    print('CSS cache erreurs JS ajoute apres set_page_config')
else:
    print('set_page_config non trouve')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
