p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Remplacer le selectbox moche par un beau menu horizontal
old = '''    # Menu de secours en haut si sidebar invisible
    page_top = st.selectbox("Menu", [
        "Tableau de bord","Moteur ARVA (Rente)","Suivi AV x 3 contrats",
        "Scenarios simulateurs","Fiscal & CAF","Declaration impots",
        "LMNP (Location Meublee) & IRL","Jalons & Actions",
        "AAH / CAF / PCH (Allocations)","Inflation","Succession",
        "Mode Senior","Bilan d exportation","BoursoBank","Crypto",
        "Annexe - Reference","Parametres","Saisie capital"],
        key="menu_top")'''

new = '''    # Menu principal
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

if old in t:
    t = t.replace(old, new)
    print('Menu stylise')
else:
    print('Pattern non trouve - on ecrit directement')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
