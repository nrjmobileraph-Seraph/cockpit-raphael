p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

lines = t.split(chr(10))
old_idx = -1
for i, l in enumerate(lines):
    if '2 0 2 6' in l and '2 0 6 7' in l and 'Garamond' in l:
        old_idx = i
        break

if old_idx >= 0:
    lines[old_idx] = '''        st.markdown('<div style="text-align:center;padding:30px 0 16px 0;"><span style="font-family:Garamond,Georgia,serif;font-size:42px;font-weight:300;font-style:italic;letter-spacing:14px;background:linear-gradient(90deg, #8B0000, #C4922A, #FFD060, #C4922A, #8B0000);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">2 0 2 6</span><span style="font-family:Garamond,Georgia,serif;font-size:28px;color:#665544;letter-spacing:6px;margin:0 24px;opacity:0.6;">&middot;&middot;&middot;</span><span style="font-family:Garamond,Georgia,serif;font-size:42px;font-weight:300;font-style:italic;letter-spacing:14px;background:linear-gradient(90deg, #8B0000, #C4922A, #FFD060, #C4922A, #8B0000);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">2 0 6 7</span><br><span style="font-family:Garamond,Georgia,serif;font-size:16px;letter-spacing:6px;font-style:italic;background:linear-gradient(90deg, #665544, #BBA888, #C4922A, #BBA888, #665544);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">&mdash; 92 ans de plan, et au-dela ...</span></div>', unsafe_allow_html=True)'''
    print(f'Banniere doublee ligne {old_idx+1}')
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
