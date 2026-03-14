p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Corriger l indentation des lignes 2082-2083
lines[2081] = '        st.markdown("## Cockpit Raphael")\n'
lines[2082] = '        st.markdown(f"**Age :** {age:.1f} ans")\n'
print('Indentation corrigee')

f=open(p,'w',encoding='utf-8')
f.writelines(lines)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
