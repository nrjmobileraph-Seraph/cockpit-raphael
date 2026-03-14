p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
fixed=0
while True:
    old_len=len(t)
    t=t.replace("f" + chr(92) + "'", "f'")
    t=t.replace(chr(92) + "'", "'")
    if len(t)==old_len:
        break
    fixed+=1
f=open(p,'w',encoding='utf-8')
f.write(t)
f.close()
print(f'Passes de correction: {fixed}')
import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {e}')
