p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Ajouter CSS pour forcer le sidebar ouvert juste apres set_page_config
old = 'initial_sidebar_state="expanded"'
new = '''initial_sidebar_state="expanded"
)
st.markdown("""<style>
    [data-testid="stSidebar"] {display: block !important; width: 300px !important; min-width: 300px !important;}
    [data-testid="stSidebar"] > div {display: block !important; width: 300px !important;}
    [data-testid="collapsedControl"] {display: block !important;}
    section[data-testid="stSidebar"] {display: block !important; opacity: 1 !important; width: 300px !important; transform: none !important;}
</style>""", unsafe_allow_html=True'''

# Attention : il faut supprimer le ) qui suit expanded" dans l original
# Trouvons la ligne complete
idx = t.find('initial_sidebar_state="expanded"')
if idx > 0:
    # Trouver la fin du set_page_config (le ) qui ferme)
    end_paren = t.find(')', idx)
    old_chunk = t[idx:end_paren+1]
    t = t.replace(old_chunk, new)
    print('CSS sidebar force ajoute')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
