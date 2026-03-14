p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Supprimer tout l'ancien systeme sidebar (Gemini v1)
old_system = '''
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True
if not st.session_state.sidebar_open:'''

# Trouver et supprimer le bloc entier
idx = t.find('if "sidebar_open" not in st.session_state:')
if idx > 0:
    # Trouver la fin du bloc else (avant with st.sidebar)
    idx_with = t.find('    with st.sidebar:', idx)
    if idx_with > 0:
        t = t[:idx] + t[idx_with:]
        print('Ancien systeme sidebar supprime')

# Supprimer le bouton Fermer dans le sidebar
t = t.replace('''        if st.button("Fermer", key="close_sb", use_container_width=True):
            st.session_state.sidebar_open = False
            st.rerun()''', '')
t = t.replace('''        if st.button("FERMER", key="close_sb", use_container_width=True):
            st.session_state.sidebar_open = False
            st.rerun()''', '')

# Supprimer header display none
t = t.replace('header[data-testid="stHeader"] { display: none !important; }', '')

# Nouveau systeme Gemini v2
gemini_v2 = '''
if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = "expanded"

if st.session_state.sidebar_state == "collapsed":
    st.markdown("""<style>
        section[data-testid="stSidebar"] { display: none !important; }
        div[data-testid="stMainBlockContainer"] > div:first-child div[data-testid="stButton"] button {
            position: fixed !important;
            top: 0.8rem !important;
            left: 1rem !important;
            width: 2.5rem !important;
            height: 2.5rem !important;
            background-color: #1a0a12 !important;
            border: 1px solid #FFD060 !important;
            color: #FFD060 !important;
            padding: 0 !important;
            z-index: 999999 !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            border-radius: 0.5rem !important;
            font-size: 1.2rem !important;
        }
        div[data-testid="stMainBlockContainer"] > div:first-child div[data-testid="stButton"] button:hover {
            background-color: #2A0A12 !important;
            box-shadow: 0 0 8px rgba(255,208,96,0.4) !important;
        }
    </style>""", unsafe_allow_html=True)
    if st.button("\\u276F"):
        st.session_state.sidebar_state = "expanded"
        st.rerun()
else:
    st.markdown("""<style>
        section[data-testid="stSidebar"] {
            display: block !important;
            visibility: visible !important;
            transform: translateX(0) !important;
            width: 300px !important;
            min-width: 300px !important;
        }
    </style>""", unsafe_allow_html=True)
'''

# Inserer avant with st.sidebar
idx_with = t.find('    with st.sidebar:')
t = t[:idx_with] + gemini_v2 + '\n' + t[idx_with:]
print('Gemini v2 installe')

# Ajouter bouton fermer discret dans sidebar
old_with = '    with st.sidebar:'
new_with = '''    with st.sidebar:
        if st.button("\\u276E", key="close_sb"):
            st.session_state.sidebar_state = "collapsed"
            st.rerun()'''
t = t.replace(old_with, new_with, 1)
print('Bouton fermer discret ajoute')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
