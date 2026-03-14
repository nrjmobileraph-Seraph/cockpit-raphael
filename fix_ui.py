with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Export bilan : le st.code() fait un fond blanc - on le remplace pas, mais on ajoute du CSS
# Le carre blanc c'est le bloc st.code() de Streamlit
code = code.replace(
    '.stException {display:none !important}',
    '.stException {display:none !important}\npre, code, .stCodeBlock {background:#1A0D12 !important; color:#FFD060 !important; border:1px solid #C4922A !important; border-radius:8px !important;}'
)

# 2. Sidebar : ajouter padding-top pour descendre sous le bouton
code = code.replace(
    'section[data-testid="stSidebarUserContent"] {{ padding-top: 4rem !important; }}',
    'section[data-testid="stSidebarUserContent"] {{ padding-top: 5rem !important; }}'
)

with open('C:/Users/BoulePiou/cockpit-raphael/app.py', 'w', encoding='utf-8') as f:
    f.write(code)

import ast
ast.parse(code)
print('SUCCES')
