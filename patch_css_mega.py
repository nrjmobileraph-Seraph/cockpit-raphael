p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver TOUS les st.markdown avec <style> et les remplacer par un seul CSS mega-force
# D'abord supprimer tous les anciens blocs CSS boutons
import re
# Compter les blocs style existants
count = t.count('stButton')
print(f'Occurrences stButton trouvees: {count}')

# Remplacer le set_page_config pour ajouter le CSS en tout premier
old_config = "st.set_page_config("
idx_config = t.find(old_config)
fin_config = t.find(")", idx_config) + 1

# Ajouter juste apres set_page_config
inject_point = fin_config
css_mega = '''
st.markdown("""<style>
/* FORCE TOUS LES BOUTONS - BORDEAUX OR */
.stButton button,
.stButton > button,
div.stButton > button,
button[kind="secondary"],
button[kind="primary"],
[data-testid="baseButton-secondary"],
[data-testid="baseButton-primary"],
.stDownloadButton button,
.stFormSubmitButton button,
section.main button,
.element-container button {
    background-color: #2A0A12 !important;
    color: #FFD060 !important;
    border: 2px solid #C4922A !important;
    font-weight: 800 !important;
    border-radius: 8px !important;
    transition: all 0.3s !important;
}
.stButton button:hover,
div.stButton > button:hover,
[data-testid="baseButton-secondary"]:hover,
[data-testid="baseButton-primary"]:hover,
section.main button:hover {
    background-color: #3A0A15 !important;
    color: #FFFFFF !important;
    border: 2px solid #FFD060 !important;
    box-shadow: 0 0 25px rgba(196,146,42,0.8) !important;
}
.stButton button:active,
.stButton button:focus {
    background-color: #2A0A12 !important;
    color: #FFD060 !important;
}
.stException {display:none !important}
</style>""", unsafe_allow_html=True)
'''

t = t[:inject_point] + '\n' + css_mega + t[inject_point:]
print('CSS mega-force injecte apres set_page_config')

# Remplacer le bouton CONNEXION par un plus joli
old_conn = 'if st.button("CONNEXION", use_container_width=True):'
new_conn = '''st.markdown('<div style="text-align:center;margin-bottom:10px;font-family:Garamond,Georgia,serif;font-size:12px;color:#665544;letter-spacing:3px;">Cliquez pour entrer</div>', unsafe_allow_html=True)
            if st.button("C O N N E X I O N", use_container_width=True):'''

t = t.replace(old_conn, new_conn)
print('Bouton CONNEXION embellit')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
