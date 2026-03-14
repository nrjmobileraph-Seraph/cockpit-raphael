p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Remplacer l'expander ferme par un expander ouvert
lines[1130] = lines[1130].replace(
    'st.markdown(' + "'" + '<div style="background:#2A1800;border:2px solid #D4A017;border-radi',
    'st.markdown(' + "'" + '<div style="background:#2A1800;border:3px solid #FFD060;border-radi'
)

# Ouvrir l'expander par defaut
lines[1131] = lines[1131].replace(
    'with st.expander("Cliquer ici pour saisir"):',
    'with st.expander("Cliquer ici pour saisir", expanded=True):'
)

f=open(p,'w',encoding='utf-8')
f.writelines(lines)
f.close()
print('Flux imprevu rendu plus visible + ouvert par defaut')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
