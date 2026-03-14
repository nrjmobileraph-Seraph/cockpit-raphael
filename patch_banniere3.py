p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

old = "st.markdown('<div style=" + '"' + "text-align:center;padding:20px 0 8px 0;"
# Trouver la ligne complete
lines = t.split(chr(10))
old_line = ''
old_idx = -1
for i, l in enumerate(lines):
    if '2026' in l and '2067' in l and 'Georgia' in l and '32px' in l:
        old_line = l
        old_idx = i
        break

if old_idx >= 0:
    lines[old_idx] = "        st.markdown('<div style=" + '"' + "text-align:center;padding:24px 0 12px 0;" + '"' + "><span style=" + '"' + "font-family:Garamond,Georgia,serif;font-size:22px;color:#C4922A;letter-spacing:10px;font-weight:300;font-style:italic;" + '"' + ">2 0 2 6</span><span style=" + '"' + "font-family:Garamond,Georgia,serif;font-size:16px;color:#665544;letter-spacing:4px;margin:0 20px;" + '"' + ">&middot;&middot;&middot;</span><span style=" + '"' + "font-family:Garamond,Georgia,serif;font-size:22px;color:#C4922A;letter-spacing:10px;font-weight:300;font-style:italic;" + '"' + ">2 0 6 7</span><span style=" + '"' + "font-family:Garamond,Georgia,serif;font-size:13px;color:#998877;letter-spacing:3px;margin-left:20px;font-style:italic;" + '"' + ">&mdash; 92 ans ...</span></div>" + "'" + ", unsafe_allow_html=True)"
    print(f'Banniere remplacee ligne {old_idx+1}')
else:
    print('Banniere non trouvee')

t = chr(10).join(lines)
f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
