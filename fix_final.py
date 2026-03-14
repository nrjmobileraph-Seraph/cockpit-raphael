with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip_backup = False
for line in lines:
    s = line.strip()
    # Supprimer import sqlite3
    if s == 'import sqlite3' or s == 'import sqlite3 as sq':
        continue
    # Supprimer DB_PATH
    if 'DB_PATH' in s and 'Path(' in s and 'cockpit.db' in s:
        continue
    # Ne PAS supprimer row_factory (ca casse l'indentation)
    # On la commente plutot
    if 'row_factory' in s:
        indent = len(line) - len(line.lstrip())
        new_lines.append(' ' * indent + '# row_factory removed\n')
        continue
    # Remplacer connexions sqlite
    if 'sqlite3.connect(' in line:
        line = line.replace("sqlite3.connect(DB_PATH)", "db_wrapper.connect()")
        line = line.replace("sqlite3.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "db_wrapper.connect()")
    if 'sq.connect(' in line:
        line = line.replace("sq.connect('C:/Users/BoulePiou/cockpit-raphael/cockpit.db')", "db_wrapper.connect()")
    if 'db_wrapper.connect(DB_PATH)' in line:
        line = line.replace('db_wrapper.connect(DB_PATH)', 'db_wrapper.connect()')
    # Remplacer backup section
    if "backup_dir = 'C:/Users/BoulePiou" in s:
        skip_backup = True
        indent = len(line) - len(line.lstrip())
        new_lines.append(' ' * indent + "st.info('Donnees sur Supabase.')\n")
        continue
    if skip_backup:
        if s.startswith('def ') or (s.startswith('st.divider') and 'Backup' not in s):
            skip_backup = False
            new_lines.append(line)
        continue
    new_lines.append(line)

code = ''.join(new_lines)

# Ajouter sys.path
code = code.replace('import streamlit as st\nimport db_wrapper', 'import streamlit as st\nimport sys, os\nsys.path.append(os.path.dirname(os.path.abspath(__file__)))\nimport db_wrapper')

# Vider init_db
import re
code = re.sub(r'def init_db\(\):.*?(?=\ndef )', 'def init_db():\n    pass\n\n', code, flags=re.DOTALL)

# Sidebar collapsed
code = code.replace('initial_sidebar_state="expanded"', 'initial_sidebar_state="collapsed"')

# Sidebar Gemini
old = '    age=age_actuel(profil); C=capital_total(cap)\n    with st.sidebar:'
new = '''    age=age_actuel(profil); C=capital_total(cap)
    TOGGLE_BTN = "position:fixed!important;top:1rem!important;left:1rem!important;width:2.5rem!important;height:2.5rem!important;background-color:#1a0a12!important;border:2px solid #FFD060!important;color:#FFD060!important;padding:0!important;z-index:999999!important;display:flex!important;align-items:center!important;justify-content:center!important;border-radius:0.5rem!important;font-size:1.2rem!important;font-weight:bold!important;line-height:1!important;"
    if "sidebar_state" not in st.session_state:
        st.session_state.sidebar_state = "expanded"
    if st.session_state.sidebar_state == "collapsed":
        st.markdown(f'<style>section[data-testid="stSidebar"]{{display:none!important;}}button[data-testid="stBaseButton-headerNoPadding"]{{display:none!important;}}div[data-testid="stMainBlockContainer"]>div:first-child div[data-testid="stButton"] button{{{TOGGLE_BTN}}}</style>', unsafe_allow_html=True)
        if st.button("\\u276F"):
            st.session_state.sidebar_state = "expanded"
            st.rerun()
    else:
        st.markdown(f'<style>section[data-testid="stSidebar"]{{display:block!important;visibility:visible!important;transform:translateX(0)!important;width:300px!important;min-width:300px!important;}}section[data-testid="stSidebarUserContent"]{{padding-top:4rem!important;}}button[data-testid="stBaseButton-headerNoPadding"]{{display:none!important;}}section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"]>div:first-child div[data-testid="stButton"] button{{{TOGGLE_BTN}}}</style>', unsafe_allow_html=True)
    with st.sidebar:
        if st.button("\\u276E", key="close_sb"):
            st.session_state.sidebar_state = "collapsed"
            st.rerun()'''
code = code.replace(old, new)

with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'w', encoding='utf-8') as f:
    f.write(code)

import ast
ast.parse(code)
print(f'ast.parse : PASS')
print(f'Pages : {code.count("def page_")}')
print(f'sqlite3 : {code.count("sqlite3")}')
print(f'BoulePiou : {code.count("BoulePiou")}')
print(f'sidebar_state : {code.count("sidebar_state")}')
print(f'db_wrapper.connect() : {code.count("db_wrapper.connect()")}')
print('SUCCES')
