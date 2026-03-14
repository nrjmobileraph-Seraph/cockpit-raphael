p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Ajouter le CSS juste apres "if not st.session_state.connected:"
old = "    if not st.session_state.connected:"
new = """    if not st.session_state.connected:
        st.markdown('''<style>
button, .stButton>button, div.stButton>button, [data-testid="stButton"]>button {
    background: #2A0A12 !important;
    color: #FFD060 !important;
    border: 2px solid #C4922A !important;
    font-size: 22px !important;
    font-weight: 800 !important;
    padding: 14px 40px !important;
    border-radius: 10px !important;
}
button:hover, .stButton>button:hover {
    background: #3A0A15 !important;
    color: #FFFFFF !important;
    border: 2px solid #FFD060 !important;
    box-shadow: 0 0 25px rgba(196,146,42,0.8) !important;
}
</style>''', unsafe_allow_html=True)"""

t = t.replace(old, new, 1)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('CSS force dans splash')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
