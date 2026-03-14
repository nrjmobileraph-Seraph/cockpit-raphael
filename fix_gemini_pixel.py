p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Remplacer le CSS du mode collapsed (bouton ouvrir)
old_collapsed = '''    st.markdown("""<style>
            section[data-testid="stSidebar"] { display: none !important; }
            div[data-testid="stMainBlockContainer"] > div:first-child div[data-testid="stButton"] button {
                position: fixed !important; top: 0.8rem !important; left: 1rem !important;
                width: 2.5rem !important; height: 2.5rem !important;
                background-color: #1a0a12 !important; border: 1px solid #FFD060 !important;
                color: #FFD060 !important; padding: 0 !important; z-index: 999999 !important;
                display: flex !important; align-items: center !important; justify-content: center !important;
                border-radius: 0.5rem !important; font-size: 1rem !important;
                width: 2.5rem !important; height: 2.5rem !important;
                top: 1rem !important; left: 1rem !important;
            }
            div[data-testid="stMainBlockContainer"] > div:first-child div[data-testid="stButton"] button:hover {
                background-color: #2A0A12 !important; box-shadow: 0 0 8px rgba(255,208,96,0.4) !important;
            }
        </style>""", unsafe_allow_html=True)'''

new_collapsed = '''    st.markdown("""<style>
            section[data-testid="stSidebar"] { display: none !important; }
            div[data-testid="stMainBlockContainer"] > div:first-child div[data-testid="stButton"] button {
                position: fixed !important;
                top: 1rem !important;
                left: 1rem !important;
                width: 2.5rem !important;
                height: 2.5rem !important;
                background-color: #1a0a12 !important;
                border: 2px solid #FFD060 !important;
                color: #FFD060 !important;
                padding: 0 !important;
                z-index: 999999 !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                border-radius: 0.5rem !important;
                font-size: 1.2rem !important;
                font-weight: bold !important;
                line-height: 1 !important;
            }
            div[data-testid="stMainBlockContainer"] > div:first-child div[data-testid="stButton"] button:hover {
                background-color: #FFD060 !important;
                color: #1a0a12 !important;
            }
        </style>""", unsafe_allow_html=True)'''

t = t.replace(old_collapsed, new_collapsed)

# Remplacer le CSS du mode expanded + bouton fermer
old_expanded = '''        st.markdown("""<style>
            section[data-testid="stSidebar"] div[data-testid="stButton"]:first-of-type button {
                background-color: #1a0a12 !important;
                border: 1.5px solid #FFD060 !important;
                color: #FFD060 !important;
                width: 2.5rem !important;
                height: 2.5rem !important;
                padding: 0 !important;
                border-radius: 0.4rem !important;
                font-size: 1rem !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                margin-top: 1rem !important;
                margin-left: 1rem !important;
            }
            section[data-testid="stSidebar"] div[data-testid="stButton"]:first-of-type button:hover {
                background-color: #2A0A12 !important;
                box-shadow: 0 0 8px rgba(255,208,96,0.4) !important;
            }
        </style>""", unsafe_allow_html=True)
        if st.button("\\u276E", key="close_sb"):'''

new_expanded = '''        st.markdown("""<style>
            section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] > div:first-child div[data-testid="stButton"] button {
                position: fixed !important;
                top: 1rem !important;
                left: 1rem !important;
                width: 2.5rem !important;
                height: 2.5rem !important;
                background-color: #1a0a12 !important;
                border: 2px solid #FFD060 !important;
                color: #FFD060 !important;
                padding: 0 !important;
                z-index: 999999 !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                border-radius: 0.5rem !important;
                font-size: 1.2rem !important;
                font-weight: bold !important;
                line-height: 1 !important;
            }
            section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] > div:first-child div[data-testid="stButton"] button:hover {
                background-color: #FFD060 !important;
                color: #1a0a12 !important;
            }
        </style>""", unsafe_allow_html=True)
        if st.button("\\u276E", key="close_sb"):'''

t = t.replace(old_expanded, new_expanded)

print('CSS Gemini pixel-perfect applique')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
