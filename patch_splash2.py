p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

old = '''def main():
    profil=get_profil(); cap=get_capital()'''

new = '''def main():
    if 'connected' not in st.session_state:
        st.session_state.connected = False
    if not st.session_state.connected:
        st.markdown('<div style="text-align:center;padding:80px 0 20px 0;"><span style="font-family:Garamond,Georgia,serif;font-size:72px;font-weight:300;font-style:italic;letter-spacing:20px;background:linear-gradient(90deg, #8B0000, #C4922A, #FFD060, #C4922A, #8B0000);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">COCKPIT</span></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;"><span style="font-family:Garamond,Georgia,serif;font-size:28px;letter-spacing:10px;background:linear-gradient(90deg, #665544, #BBA888, #C4922A, #BBA888, #665544);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">P A T R I M O N I A L</span></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;padding:30px 0;"><span style="font-family:Garamond,Georgia,serif;font-size:18px;color:#BBA888;font-style:italic;letter-spacing:4px;">2026 &middot;&middot;&middot; 2067</span></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;padding:0 0 40px 0;"><span style="font-family:Georgia,serif;font-size:14px;color:#665544;">v4.3 &mdash; Raphael</span></div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns([2, 1, 2])
        with c2:
            if st.button("CONNEXION"):
                st.session_state.connected = True
                st.rerun()
        return
    profil=get_profil(); cap=get_capital()'''

if old in t:
    t = t.replace(old, new)
    print('Splash insere dans main()')
else:
    print('main() non trouve')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
