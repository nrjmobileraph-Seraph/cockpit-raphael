p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
# Changer initial_sidebar_state en collapsed pour Render
t = t.replace('initial_sidebar_state="expanded"', 'initial_sidebar_state="collapsed"')
print('Sidebar collapsed par defaut')
f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
