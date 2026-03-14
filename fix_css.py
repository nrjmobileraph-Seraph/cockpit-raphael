p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Supprimer toutes les lignes stException mal placees
lines = t.split(chr(10))
clean = []
for l in lines:
    if 'stException' in l:
        continue
    if l.strip() == 'pass' and len(clean) > 0 and 'stException' in (clean[-1] if clean else ''):
        continue
    clean.append(l)
t = chr(10).join(clean)

# Ajouter le CSS une seule fois, dans main(), juste apres init_db()
t = t.replace('init_db()', 'init_db()\n    st.markdown(\'<style>div[data-testid="stException"]{display:none !important;}</style>\', unsafe_allow_html=True)')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('CSS nettoye et replace')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:200]}')
