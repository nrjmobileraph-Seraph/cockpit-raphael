p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Trouver le st.markdown avec le CSS
# Remplacer tout le bloc CSS par un CSS ultra-force
old_style = 'st.markdown("<style>.stException{display:none !important}'
# Trouver la fin de cette ligne
idx = t.find(old_style)
fin = t.find('</style>"', idx) + len('</style>"')
old_full = t[idx:fin]

new_full = '''st.markdown("""<style>
.stException{display:none !important}
button, .stButton>button, div.stButton>button, [data-testid="stButton"]>button,
.stDownloadButton>button, div[data-testid="stFormSubmitButton"]>button {
    background: #2A0A12 !important;
    color: #FFD060 !important;
    border: 2px solid #C4922A !important;
    font-size: 18px !important;
    font-weight: 800 !important;
    padding: 10px 24px !important;
    border-radius: 8px !important;
    transition: all 0.3s !important;
}
button:hover, .stButton>button:hover, div.stButton>button:hover {
    background: #3A0A15 !important;
    color: #FFFFFF !important;
    border: 2px solid #FFD060 !important;
    transform: scale(1.05) !important;
    box-shadow: 0 0 25px rgba(196,146,42,0.8) !important;
}
button:focus, .stButton>button:focus {
    background: #2A0A12 !important;
    color: #FFD060 !important;
    border: 2px solid #C4922A !important;
}
</style>"""'''

if old_full:
    t = t.replace(old_full, new_full)
    print('CSS global boutons force')
else:
    print('CSS non trouve')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
