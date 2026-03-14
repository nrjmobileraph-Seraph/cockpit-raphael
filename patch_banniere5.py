p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Doubler les tailles
t = t.replace('font-size:42px;font-weight:300;font-style:italic;letter-spacing:14px;background:linear-gradient', 'font-size:72px;font-weight:300;font-style:italic;letter-spacing:20px;background:linear-gradient')
t = t.replace('font-size:28px;color:#665544;letter-spacing:6px;margin:0 24px', 'font-size:44px;color:#665544;letter-spacing:10px;margin:0 30px')
t = t.replace('font-size:16px;letter-spacing:6px;font-style:italic;background:linear-gradient', 'font-size:28px;letter-spacing:8px;font-style:italic;background:linear-gradient')

f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print('Tailles doublees')

import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:300]}')
