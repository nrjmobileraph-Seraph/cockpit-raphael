p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Styler le bouton ouvrir (mode collapsed)
old_open = '''                background-color: #1a0a12 !important; border: 1px solid #FFD060 !important;
                color: #FFD060 !important; padding: 0 !important; z-index: 999999 !important;
                display: flex !important; align-items: center !important; justify-content: center !important;
                border-radius: 0.5rem !important; font-size: 1.2rem !important;'''

new_open = '''                background-color: #1a0a12 !important; border: 1.5px solid #FFD060 !important;
                color: #FFD060 !important; padding: 0 !important; z-index: 999999 !important;
                display: flex !important; align-items: center !important; justify-content: center !important;
                border-radius: 0.4rem !important; font-size: 1rem !important;
                width: 2rem !important; height: 2rem !important;
                top: 0.5rem !important; left: 0.5rem !important;'''

t = t.replace(old_open, new_open)

# Styler le bouton fermer dans le sidebar
old_close = '''        if st.button("\\u276E", key="close_sb"):'''
new_close = '''        st.markdown("""<style>
            section[data-testid="stSidebar"] div[data-testid="stButton"]:first-of-type button {
                background-color: #1a0a12 !important;
                border: 1.5px solid #FFD060 !important;
                color: #FFD060 !important;
                width: 2rem !important;
                height: 2rem !important;
                padding: 0 !important;
                border-radius: 0.4rem !important;
                font-size: 1rem !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                margin-top: 0.5rem !important;
                margin-left: 0.3rem !important;
            }
            section[data-testid="stSidebar"] div[data-testid="stButton"]:first-of-type button:hover {
                background-color: #2A0A12 !important;
                box-shadow: 0 0 8px rgba(255,208,96,0.4) !important;
            }
        </style>""", unsafe_allow_html=True)
        if st.button("\\u276E", key="close_sb"):'''

t = t.replace(old_close, new_close)
print('Boutons alignes et stylises')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
