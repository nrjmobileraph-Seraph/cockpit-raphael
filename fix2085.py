p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Verifier si la ligne 2085 est complete
line = lines[2084]
if line.count("'") % 2 != 0:
    # Ligne tronquee - la fermer
    lines[2084] = line.rstrip() + "</span></div>', unsafe_allow_html=True)\n"
    print('Ligne 2085 reparee')

f=open(p,'w',encoding='utf-8')
f.writelines(lines)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
