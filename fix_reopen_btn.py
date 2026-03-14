p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Ajouter CSS pour agrandir le bouton de reouverture
css_btn = '''
    /* Bouton > pour rouvrir le sidebar - GROS ET VISIBLE */
    [data-testid="collapsedControl"] {
        position: fixed !important;
        top: 10px !important;
        left: 10px !important;
        z-index: 9999 !important;
        background: #1a0a12 !important;
        border: 2px solid #FFD060 !important;
        border-radius: 10px !important;
        padding: 12px 16px !important;
        font-size: 28px !important;
        color: #FFD060 !important;
    }
'''

# Trouver le premier st.markdown CSS et ajouter dedans
old_style = '/* FORCE TOUS LES BOUTONS - BORDEAUX OR */'
if old_style in t:
    t = t.replace(old_style, css_btn + '\n' + old_style)
    print('CSS bouton reouverture ajoute')
else:
    print('Pattern CSS non trouve, ajout apres set_page_config')
    t = t.replace('initial_sidebar_state="expanded"', 'initial_sidebar_state="expanded"\n)\nst.markdown("""<style>' + css_btn + '</style>""", unsafe_allow_html=True')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
