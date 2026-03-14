p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Ligne 451 (index 450) doit etre indentee de 8 espaces
lines[450] = '        titre("COCKPIT PATRIMONIAL - PHASE CONSTRUCTION")\n'

f=open(p,'w',encoding='utf-8')
f.writelines(lines)
f.close()
print('Indentation corrigee')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
