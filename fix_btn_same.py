p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Bouton ouvrir : forcer taille et position
old_open = '''                width: 2rem !important; height: 2rem !important;
                top: 0.5rem !important; left: 0.5rem !important;'''

new_open = '''                width: 2.5rem !important; height: 2.5rem !important;
                top: 1rem !important; left: 1rem !important;'''

t = t.replace(old_open, new_open)

# Bouton fermer : forcer meme taille et position
old_close = '''                width: 2rem !important;
                height: 2rem !important;
                padding: 0 !important;
                border-radius: 0.4rem !important;
                font-size: 1rem !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                margin-top: 0.5rem !important;
                margin-left: 0.3rem !important;'''

new_close = '''                width: 2.5rem !important;
                height: 2.5rem !important;
                padding: 0 !important;
                border-radius: 0.4rem !important;
                font-size: 1rem !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                margin-top: 1rem !important;
                margin-left: 1rem !important;'''

t = t.replace(old_close, new_close)
print('Boutons identiques')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
