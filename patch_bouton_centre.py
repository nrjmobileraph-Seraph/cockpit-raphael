p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

old = """        c1, c2, c3 = st.columns([2, 1, 2])
        with c2:
            if st.button("CONNEXION"):"""

new = """        st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns([3, 2, 3])
        with c2:
            if st.button("CONNEXION", use_container_width=True):"""

t = t.replace(old, new)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Bouton centre')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
