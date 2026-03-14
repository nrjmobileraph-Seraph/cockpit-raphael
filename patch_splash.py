p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Ajouter un ecran d'accueil avant le menu
old_main = '    init_db()'
new_main = '''    if 'connected' not in st.session_state:
        st.session_state.connected = False

    if not st.session_state.connected:
        st.markdown('<div style="text-align:center;padding:60px 0 20px 0;"><span style="font-family:Garamond,Georgia,serif;font-size:72px;font-weight:300;font-style:italic;letter-spacing:20px;background:linear-gradient(90deg, #8B0000, #C4922A, #FFD060, #C4922A, #8B0000);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">COCKPIT</span></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;padding:0 0 10px 0;"><span style="font-family:Garamond,Georgia,serif;font-size:28px;letter-spacing:10px;background:linear-gradient(90deg, #665544, #BBA888, #C4922A, #BBA888, #665544);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">P A T R I M O N I A L</span></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;padding:20px 0;"><span style="font-family:Garamond,Georgia,serif;font-size:18px;color:#BBA888;font-style:italic;letter-spacing:4px;">2026 &middot;&middot;&middot; 2067 &mdash; 92 ans de plan</span></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;padding:10px 0 40px 0;"><span style="font-family:Georgia,serif;font-size:14px;color:#665544;">v4.3 &mdash; 12 mars 2026 &mdash; Raphael</span></div>', unsafe_allow_html=True)
        col_l, col_c, col_r = st.columns([2, 1, 2])
        with col_c:
            if st.button("CONNEXION", key="splash_connect"):
                st.session_state.connected = True
                st.rerun()
        return

    init_db()'''

t = t.replace(old_main, new_main)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Page accueil splash installee')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
