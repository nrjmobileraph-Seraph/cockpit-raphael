p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Trouver le bloc sidebar et tout wrapper
new_lines = []
in_sidebar = False
sidebar_start = -1

for i, l in enumerate(lines):
    if 'with st.sidebar:' in l:
        in_sidebar = True
        sidebar_start = i
        new_lines.append(l)
        new_lines.append('        try:\n')
        continue
    
    if in_sidebar and 'page=st.radio' in l:
        # Fermer le try avant le radio
        new_lines.append('        except Exception as e:\n')
        new_lines.append('            st.warning(f"Erreur sidebar: {e}")\n')
        in_sidebar = False
        new_lines.append(l)
        continue
    
    if in_sidebar and sidebar_start >= 0:
        # Ajouter 4 espaces d indentation
        if l.strip():
            new_lines.append('    ' + l)
        else:
            new_lines.append(l)
        continue
    
    new_lines.append(l)

f=open(p,'w',encoding='utf-8')
f.writelines(new_lines)
f.close()
print('Sidebar wrap complet')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
