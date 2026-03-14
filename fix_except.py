p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()

# Supprimer lignes 2100 et 2101
del lines[2100]  # st.markdown doublon
del lines[2099]  # except:
print('except orphelin supprime')

f=open(p,'w',encoding='utf-8')
f.writelines(lines)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
