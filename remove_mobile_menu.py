p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Supprimer lignes 2122 a 2127 (index 2121 a 2126)
del lines[2121:2127]
print('Menu mobile supprime (lignes 2122-2127)')

f=open(p,'w',encoding='utf-8')
f.writelines(lines)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
