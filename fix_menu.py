p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Corriger la ligne cassee
old = '        "Parametres","Saisie capital":        lambda: page_saisie(profil,cap),'
new = '''        "Parametres":              lambda: page_parametres(profil,cap),
        "Saisie capital":          lambda: page_saisie(profil,cap),'''

t = t.replace(old, new)
print('Menu corrige')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
