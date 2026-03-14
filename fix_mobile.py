p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
# Trouver le CSS existant apres set_page_config et ajouter le responsive mobile
old_css = '[data-testid="collapsedControl"] {display: block !important;}'
new_css = '''[data-testid="collapsedControl"] {display: block !important;}
    @media (max-width: 768px) {
        [data-testid="stSidebar"] {width: 70vw !important; min-width: 200px !important; max-width: 280px !important; z-index: 999 !important;}
        [data-testid="stSidebar"][aria-expanded="false"] {display: none !important; margin-left: -300px !important;}
        .main .block-container {padding: 1rem 0.5rem !important;}
        [data-testid="collapsedControl"] {display: block !important; position: fixed !important; top: 5px !important; left: 5px !important; z-index: 9999 !important; background: #1a0a12 !important; border: 2px solid #FFD060 !important; border-radius: 8px !important; padding: 8px 12px !important; font-size: 24px !important;}
    }'''
t = t.replace(old_css, new_css)
print('CSS mobile ajoute')
f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
