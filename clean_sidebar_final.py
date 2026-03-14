p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# 1. Remettre expanded
t = t.replace('initial_sidebar_state="collapsed"', 'initial_sidebar_state="expanded"')

# 2. Supprimer TOUT le CSS qui touche au sidebar
import re
lines = t.split('\n')
new_lines = []
skip = False
for line in lines:
    low = line.lower()
    if 'stsidebar' in low or 'collapsedcontrol' in low or 'stsidebar' in low:
        continue
    if 'mobile-only' in low:
        continue
    if 'mobile_nav' in low or 'mob_nav' in low or 'page_mobile' in low:
        continue
    if 'session_state.page' in line and 'page_mobile' in line:
        continue
    new_lines.append(line)

t = '\n'.join(new_lines)
print('CSS sidebar nettoye')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
