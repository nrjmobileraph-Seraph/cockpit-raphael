p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Rendre le bouton hamburger beau
old_btn_css = '''    st.markdown("""<style>
        section[data-testid="stSidebar"] { display: none !important; }
    </style>""", unsafe_allow_html=True)'''

new_btn_css = '''    st.markdown("""<style>
        section[data-testid="stSidebar"] { display: none !important; }
        div[data-testid="stButton"] button[kind="secondary"] {
            background: #1a0a12 !important;
            color: #FFD060 !important;
            border: 2px solid #FFD060 !important;
            border-radius: 10px !important;
            font-size: 28px !important;
            padding: 8px 16px !important;
            box-shadow: 0 4px 8px rgba(0,0,0,0.4) !important;
        }
        div[data-testid="stButton"] button[kind="secondary"]:hover {
            background: #2A0A12 !important;
            transform: scale(1.05) !important;
        }
    </style>""", unsafe_allow_html=True)'''

t = t.replace(old_btn_css, new_btn_css)

# Rendre le bouton Fermer beau
old_fermer = '''        if st.button("Fermer", key="close_sb", use_container_width=True):'''
new_fermer = '''        st.markdown("""<style>
            div[data-testid="stSidebar"] button[kind="secondary"] {
                background: #1a0a12 !important;
                color: #FFD060 !important;
                border: 2px solid #FFD060 !important;
                border-radius: 8px !important;
                font-weight: bold !important;
            }
        </style>""", unsafe_allow_html=True)
        if st.button("FERMER LE MENU", key="close_sb", use_container_width=True):'''

t = t.replace(old_fermer, new_fermer)

# Changer le symbole du bouton ouvrir
t = t.replace('if st.button("\\u2630", key="open_sb"):', 'if st.button("MENU", key="open_sb"):')

print('Boutons stylises')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
