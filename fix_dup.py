p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Supprimer TOUS les anciens boutons fermer
t = t.replace('''        st.markdown("""<style>
            div[data-testid="stSidebar"] button[kind="secondary"] {
                background: #1a0a12 !important;
                color: #FFD060 !important;
                border: 2px solid #FFD060 !important;
                border-radius: 8px !important;
                font-weight: bold !important;
            }
        </style>""", unsafe_allow_html=True)
        if st.button("FERMER LE MENU", key="close_sb", use_container_width=True):
            st.session_state.sidebar_open = False
            st.rerun()''', '')

t = t.replace('''        if st.button("FERMER LE MENU", key="close_sb", use_container_width=True):
            st.session_state.sidebar_open = False
            st.rerun()''', '')

print(f'close_sb restants: {t.count("close_sb")}')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
