p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Styler le bouton MENU en bordeaux/or au lieu de blanc
old = '''    col1, col2 = st.columns([1, 20])
    with col1:
        if st.button("\\u2630", key="open_sb"):'''

new = '''    st.markdown("""<style>
        div[data-testid="stMainBlockContainer"] div[data-testid="stButton"]:first-of-type button {
            background: linear-gradient(135deg, #1a0a12, #2A0A12) !important;
            color: #FFD060 !important;
            border: 2px solid #FFD060 !important;
            border-radius: 10px !important;
            font-size: 20px !important;
            padding: 8px 20px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5) !important;
            letter-spacing: 2px !important;
            font-weight: bold !important;
        }
        div[data-testid="stMainBlockContainer"] div[data-testid="stButton"]:first-of-type button:hover {
            background: linear-gradient(135deg, #3A1A22, #4A2A32) !important;
            box-shadow: 0 4px 16px rgba(255,208,96,0.3) !important;
        }
    </style>""", unsafe_allow_html=True)
    if st.button("M E N U", key="open_sb"):'''

t = t.replace(old, new)

# Aussi styler le bouton Fermer
old2 = '        if st.button("Fermer", key="close_sb", use_container_width=True):'
new2 = '''        st.markdown("""<style>
            div[data-testid="stSidebar"] div[data-testid="stButton"]:first-of-type button {
                background: linear-gradient(135deg, #1a0a12, #2A0A12) !important;
                color: #FFD060 !important;
                border: 2px solid #FFD060 !important;
                border-radius: 8px !important;
                font-weight: bold !important;
                letter-spacing: 2px !important;
            }
        </style>""", unsafe_allow_html=True)
        if st.button("F E R M E R", key="close_sb", use_container_width=True):'''

t = t.replace(old2, new2)

print('Boutons bordeaux/or')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
