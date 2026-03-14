p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Remplacer le CSS mobile par un qui cache le sidebar sur petit ecran
old_css = '''@media (max-width: 768px) {
        [data-testid="stSidebar"] {width: 70vw !important; min-width: 200px !important; max-width: 280px !important; z-index: 999 !important;}
        [data-testid="stSidebar"][aria-expanded="false"] {display: none !important; margin-left: -300px !important;}
        .main .block-container {padding: 1rem 0.5rem !important;}
        [data-testid="collapsedControl"] {display: block !important; position: fixed !important; top: 5px !important; left: 5px !important; z-index: 9999 !important; background: #1a0a12 !important; border: 2px solid #FFD060 !important; border-radius: 8px !important; padding: 8px 12px !important; font-size: 24px !important;}
    }'''

new_css = '''@media (max-width: 768px) {
        [data-testid="stSidebar"] {display: none !important;}
        [data-testid="collapsedControl"] {display: none !important;}
        .main .block-container {padding: 0.5rem !important; max-width: 100% !important;}
    }'''

t = t.replace(old_css, new_css)

# Ajouter un menu mobile en haut de page dans le main
old_sidebar = '    with st.sidebar:'
new_sidebar = '''    # Menu mobile (visible seulement sur petit ecran)
    st.markdown("""<style>
        @media (min-width: 769px) { .mobile-menu { display: none !important; } }
        @media (max-width: 768px) { .mobile-menu { display: block !important; } }
    </style>""", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="mobile-menu">', unsafe_allow_html=True)
        page_mobile = st.selectbox("Navigation", [
            "Tableau de bord","Moteur ARVA (Rente)","Suivi AV x 3 contrats",
            "Scenarios simulateurs","Fiscal & CAF","Declaration impots",
            "LMNP (Location Meublee) & IRL","Jalons & Actions",
            "AAH / CAF / PCH (Allocations)","Inflation","Succession",
            "Mode Senior","Bilan d exportation","BoursoBank","Crypto",
            "Annexe - Reference","Parametres","Saisie capital"],
            key="mobile_nav")
        st.markdown('</div>', unsafe_allow_html=True)
    with st.sidebar:'''

t = t.replace(old_sidebar, new_sidebar, 1)

# Utiliser page_mobile si page n'est pas defini
old_dispatch = '    {\n        "Tableau de bord":'
new_dispatch = '    page = page if "page" in dir() and page else page_mobile\n    {\n        "Tableau de bord":'
t = t.replace(old_dispatch, new_dispatch, 1)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Menu mobile ajoute')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
