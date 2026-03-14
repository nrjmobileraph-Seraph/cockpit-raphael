p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Ajouter un selectbox en haut de page en plus du sidebar
old = '    with st.sidebar:'
new = '''    # Menu de secours en haut si sidebar invisible
    page_top = st.selectbox("Menu", [
        "Tableau de bord","Moteur ARVA (Rente)","Suivi AV x 3 contrats",
        "Scenarios simulateurs","Fiscal & CAF","Declaration impots",
        "LMNP (Location Meublee) & IRL","Jalons & Actions",
        "AAH / CAF / PCH (Allocations)","Inflation","Succession",
        "Mode Senior","Bilan d exportation","BoursoBank","Crypto",
        "Annexe - Reference","Parametres","Saisie capital"],
        key="menu_top")
    with st.sidebar:'''

t = t.replace(old, new, 1)

# Utiliser page_top au lieu de page si sidebar rate
old2 = '''        st.caption("v4.3 - Mars 2026")
    {'''
new2 = '''        st.caption("v4.3 - Mars 2026")
    page = page if 'page' in dir() else page_top
    {'''

t = t.replace(old2, new2)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Menu de secours ajoute')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
