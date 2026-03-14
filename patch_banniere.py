p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Ajouter juste apres init_db() et le CSS
old = '    st.markdown("<style>.stException{display:none !important}</style>", unsafe_allow_html=True)'
new = '''    st.markdown("<style>.stException{display:none !important}</style>", unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;padding:12px 0 4px 0;"><span style="font-family:Georgia,serif;font-size:15px;color:#BBA888;letter-spacing:6px;font-style:italic;">2026</span><span style="font-family:Georgia,serif;font-size:13px;color:#665544;letter-spacing:4px;font-style:italic;"> &middot;&middot;&middot; </span><span style="font-family:Georgia,serif;font-size:15px;color:#BBA888;letter-spacing:6px;font-style:italic;">2067</span><span style="font-family:Georgia,serif;font-size:11px;color:#665544;font-style:italic;"> &mdash; 92 ans ...</span></div>', unsafe_allow_html=True)'''

t = t.replace(old, new)

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Banniere installee')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
