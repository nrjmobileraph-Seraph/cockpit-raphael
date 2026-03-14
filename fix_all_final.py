p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

import re

# 1. Nettoyer chemins Windows
t = re.sub(r"db_wrapper\.connect\(['\"]C:.*?['\"]\)", "db_wrapper.connect()", t)
t = t.replace("backup_dir = 'C:/Users/BoulePiou/cockpit-raphael/backups'", "backup_dir = os.path.join(os.path.dirname(__file__), 'backups')")
t = t.replace("shutil.copy2('C:/Users/BoulePiou/cockpit-raphael/cockpit.db', bp)", "pass")
t = t.replace("shutil.copy2(os.path.join(backup_dir, choix), 'C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "pass")
print(f'BoulePiou: {t.count("BoulePiou")}')

# 2. Supprimer tout CSS stSidebar existant
lines = t.split('\n')
new_lines = []
for line in lines:
    if 'stSidebar' in line and ('display' in line or 'width' in line or 'transform' in line or 'visibility' in line):
        continue
    if 'collapsedControl' in line:
        continue
    new_lines.append(line)
t = '\n'.join(new_lines)

# 3. Ajouter systeme Gemini DANS main(), juste avant with st.sidebar
gemini = '''
    # === SIDEBAR TOGGLE (Gemini) ===
    if "sidebar_state" not in st.session_state:
        st.session_state.sidebar_state = "expanded"
    if st.session_state.sidebar_state == "collapsed":
        st.markdown("""<style>
            section[data-testid="stSidebar"] { display: none !important; }
            div[data-testid="stMainBlockContainer"] > div:first-child div[data-testid="stButton"] button {
                position: fixed !important; top: 0.8rem !important; left: 1rem !important;
                width: 2.5rem !important; height: 2.5rem !important;
                background-color: #1a0a12 !important; border: 1px solid #FFD060 !important;
                color: #FFD060 !important; padding: 0 !important; z-index: 999999 !important;
                display: flex !important; align-items: center !important; justify-content: center !important;
                border-radius: 0.5rem !important; font-size: 1.2rem !important;
            }
            div[data-testid="stMainBlockContainer"] > div:first-child div[data-testid="stButton"] button:hover {
                background-color: #2A0A12 !important; box-shadow: 0 0 8px rgba(255,208,96,0.4) !important;
            }
        </style>""", unsafe_allow_html=True)
        if st.button("\\u276F"):
            st.session_state.sidebar_state = "expanded"
            st.rerun()
    else:
        st.markdown("""<style>
            section[data-testid="stSidebar"] {
                display: block !important; visibility: visible !important;
                transform: translateX(0) !important; width: 300px !important; min-width: 300px !important;
            }
        </style>""", unsafe_allow_html=True)

'''

# Trouver "    with st.sidebar:" dans main()
idx = t.find('    with st.sidebar:')
if idx > 0:
    t = t[:idx] + gemini + t[idx:]
    print('Gemini insere avant with st.sidebar')

# 4. Ajouter bouton fermer dans sidebar
old = '    with st.sidebar:'
new = '''    with st.sidebar:
        if st.button("\\u276E", key="close_sb"):
            st.session_state.sidebar_state = "collapsed"
            st.rerun()'''
t = t.replace(old, new, 1)
print('Bouton fermer ajoute')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
