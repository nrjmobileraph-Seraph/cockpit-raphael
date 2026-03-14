p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Changer M E N U en MENU et elargir
t = t.replace('"M E N U"', '"MENU"')
t = t.replace('"F E R M E R"', '"FERMER"')

# Elargir le bouton
t = t.replace('padding: 8px 20px', 'padding: 10px 30px')

print('Bouton elargi')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
