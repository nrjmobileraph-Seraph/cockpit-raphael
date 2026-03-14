p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Ajouter un try/except autour de profil=get_profil()
old = '    profil=get_profil(); cap=get_capital()'
new = '''    try:
        profil=get_profil(); cap=get_capital()
    except Exception as e:
        st.error(f"Erreur connexion base : {e}")
        st.stop()'''

t = t.replace(old, new)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Erreurs visibles')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
