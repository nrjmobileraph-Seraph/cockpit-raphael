p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Remplacer tout le bloc sidebar par un sidebar simple et solide
old_sidebar_start = '    with st.sidebar:'
# Trouver le debut et la fin du bloc sidebar
idx_start = t.find('    with st.sidebar:')
idx_radio_end = t.find("        st.caption(\"v4.3 - Mars 2026\")")
if idx_radio_end > 0:
    idx_end = t.find('\n', idx_radio_end) + 1
    
    old_block = t[idx_start:idx_end]
    
    new_block = '''    with st.sidebar:
        st.markdown('<div style="text-align:center;padding:10px;"><span style="color:#FFD060;font-size:20px;font-weight:bold;">COCKPIT RAPHAEL</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align:center;color:#BBA888;">Age : {age:.1f} ans | Capital : {C:,.0f} EUR</div>', unsafe_allow_html=True)
        st.markdown("---")
        page=st.radio("Navigation",[
            "Tableau de bord",
            "Moteur ARVA (Rente)",
            "Suivi AV x 3 contrats",
            "Scenarios simulateurs",
            "Fiscal & CAF",
            "Declaration impots",
            "LMNP (Location Meublee) & IRL",
            "Jalons & Actions",
            "AAH / CAF / PCH (Allocations)",
            "Inflation",
            "Succession",
            "Mode Senior",
            "Bilan d exportation",
            "BoursoBank",
            "Crypto",
            "Annexe - Reference",
            "Parametres","Saisie capital",
        ])
        st.markdown("---")
        st.caption("v4.3 - Mars 2026")'''
    
    t = t.replace(old_block, new_block)
    print('Sidebar remplace')

# Supprimer le menu top (plus besoin)
old_top = '''    # Menu principal
    pages_list = [
        "Tableau de bord","Moteur ARVA (Rente)","Suivi AV x 3 contrats",
        "Scenarios simulateurs","Fiscal & CAF","Declaration impots",
        "LMNP (Location Meublee) & IRL","Jalons & Actions",
        "AAH / CAF / PCH (Allocations)","Inflation","Succession",
        "Mode Senior","Bilan d exportation","BoursoBank","Crypto",
        "Annexe - Reference","Parametres","Saisie capital"]
    st.markdown("""<style>
        div[data-testid="stSelectbox"] > div > div {background:#1a0a12 !important; color:#FFD060 !important; border:1px solid #FFD060 !important; border-radius:8px;}
        div[data-testid="stSelectbox"] label {color:#FFD060 !important; font-weight:bold;}
    </style>""", unsafe_allow_html=True)
    page_top = st.selectbox("NAVIGATION", pages_list, key="menu_top")'''

t = t.replace(old_top, '')
print('Menu top supprime')

# Aussi supprimer la ligne page = page if
t = t.replace("    page = page if 'page' in dir() else page_top", '')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
