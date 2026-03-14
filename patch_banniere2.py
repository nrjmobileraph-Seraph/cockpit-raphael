p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

old = '        titre("COCKPIT PATRIMONIAL - PHASE CONSTRUCTION")'
new = '''        st.markdown('<div style="text-align:center;padding:20px 0 8px 0;"><div style="font-family:Georgia,serif;font-size:32px;color:#C4922A;letter-spacing:8px;font-weight:300;font-style:italic;">2026</div><div style="font-family:Georgia,serif;font-size:14px;color:#665544;letter-spacing:3px;margin:6px 0;">&middot; &middot; &middot;</div><div style="font-family:Georgia,serif;font-size:32px;color:#C4922A;letter-spacing:8px;font-weight:300;font-style:italic;">2067</div><div style="font-family:Georgia,serif;font-size:12px;color:#BBA888;letter-spacing:4px;margin-top:8px;font-style:italic;">92 ans de plan &mdash; et au-dela ...</div></div>', unsafe_allow_html=True)
        titre("COCKPIT PATRIMONIAL - PHASE CONSTRUCTION")'''

t = t.replace(old, new)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Banniere premiere page installee')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
