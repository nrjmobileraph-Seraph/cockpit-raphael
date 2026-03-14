import re

with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Ajouter sys.path avant db_wrapper
code = code.replace('import streamlit as st\nimport db_wrapper', 'import streamlit as st\nimport sys, os\nsys.path.append(os.path.dirname(os.path.abspath(__file__)))\nimport db_wrapper')

# 2. Supprimer sqlite3
code = code.replace('import sqlite3\n', '')
code = code.replace('import sqlite3 as sq\n', '')
code = code.replace('    import sqlite3\n', '')

# 3. Supprimer DB_PATH
code = code.replace("DB_PATH = Path(__file__).parent / \"cockpit.db\"\n", '')

# 4. Remplacer toutes les connexions
code = code.replace('sqlite3.connect(DB_PATH)', 'db_wrapper.connect()')
code = code.replace('db_wrapper.connect(DB_PATH)', 'db_wrapper.connect()')
code = re.sub(r"sqlite3\.connect\(['\"].*?cockpit\.db['\"].*?\)", 'db_wrapper.connect()', code)

# 5. Supprimer row_factory
code = re.sub(r'.*row_factory.*\n', '', code)

# 6. Supprimer chemins BoulePiou dans backup
old_backup = '''    st.divider()
    st.subheader("Backup et restauration")
    import os
    backup_dir = 'C:/Users/BoulePiou/cockpit-raphael/backups\''''
if old_backup in code:
    # Find and replace the whole backup section
    start = code.find('    st.divider()\n    st.subheader("Backup et restauration")\n    import os\n    backup_dir')
    if start >= 0:
        end = code.find('\ndef page_export', start)
        if end >= 0:
            code = code[:start] + '    st.divider()\n    st.subheader("Backup et restauration")\n    st.info("Les donnees sont hebergees sur Supabase (PostgreSQL cloud).")\n\n' + code[end:]

# 7. Vider init_db
old_init = code[code.find('def init_db():'):code.find('\ndef get_profil')]
code = code.replace(old_init, 'def init_db():\n    pass\n')

# 8. initial_sidebar_state collapsed
code = code.replace('initial_sidebar_state="expanded"', 'initial_sidebar_state="collapsed"')

# 9. Ajouter sidebar Gemini - chercher "age=age_actuel(profil); C=capital_total(cap)\n    with st.sidebar:"
old_sidebar = '    age=age_actuel(profil); C=capital_total(cap)\n    with st.sidebar:'
new_sidebar = '''    age=age_actuel(profil); C=capital_total(cap)
    # === SIDEBAR TOGGLE (solution Gemini) ===
    TOGGLE_BTN = "position:fixed!important;top:1rem!important;left:1rem!important;width:2.5rem!important;height:2.5rem!important;background-color:#1a0a12!important;border:2px solid #FFD060!important;color:#FFD060!important;padding:0!important;z-index:999999!important;display:flex!important;align-items:center!important;justify-content:center!important;border-radius:0.5rem!important;font-size:1.2rem!important;font-weight:bold!important;line-height:1!important;"
    if "sidebar_state" not in st.session_state:
        st.session_state.sidebar_state = "expanded"
    if st.session_state.sidebar_state == "collapsed":
        st.markdown(f'<style>section[data-testid="stSidebar"]{{display:none!important;}}button[data-testid="stBaseButton-headerNoPadding"]{{display:none!important;}}[data-testid="stSidebarCollapseButton"]{{display:none!important;}}div[data-testid="stMainBlockContainer"]>div:first-child div[data-testid="stButton"] button{{{TOGGLE_BTN}}}</style>', unsafe_allow_html=True)
        if st.button("\\u276F"):
            st.session_state.sidebar_state = "expanded"
            st.rerun()
    else:
        st.markdown(f'<style>section[data-testid="stSidebar"]{{display:block!important;visibility:visible!important;transform:translateX(0)!important;width:300px!important;min-width:300px!important;}}section[data-testid="stSidebarUserContent"]{{padding-top:4rem!important;}}button[data-testid="stBaseButton-headerNoPadding"]{{display:none!important;}}[data-testid="stSidebarCollapseButton"]{{display:none!important;}}section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"]>div:first-child div[data-testid="stButton"] button{{{TOGGLE_BTN}}}</style>', unsafe_allow_html=True)
    with st.sidebar:
        if st.button("\\u276E", key="close_sb"):
            st.session_state.sidebar_state = "collapsed"
            st.rerun()'''
code = code.replace(old_sidebar, new_sidebar)

with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'w', encoding='utf-8') as f:
    f.write(code)

# Verify
import ast
ast.parse(code)
pages = code.count('def page_')
sq = code.count('sqlite3')
db = code.count('DB_PATH')
bp = code.count('BoulePiou')
sb = code.count('sidebar_state')
print(f'ast.parse : PASS')
print(f'Pages : {pages}')
print(f'sqlite3 : {sq}')
print(f'DB_PATH : {db}')
print(f'BoulePiou : {bp}')
print(f'sidebar_state : {sb}')
print('SUCCES')
