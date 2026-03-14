p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
lines=f.readlines()
f.close()
fixed=0
for i in range(len(lines)):
    if 'stException' in lines[i]:
        # Verifier la ligne avant - si c'est un if/else, ajouter un pass
        if i > 0 and ('if ' in lines[i-1] or 'else' in lines[i-1]):
            indent = len(lines[i]) - len(lines[i].lstrip())
            lines[i] = ' ' * indent + 'pass' + chr(10) + lines[i]
            fixed += 1
        # Fixer l'indentation
        lines[i] = '    ' + lines[i].lstrip()
        fixed += 1
f=open(p,'w',encoding='utf-8')
f.writelines(lines)
f.close()
print(f'Corrections: {fixed}')
import py_compile
try:
    py_compile.compile(p, doraise=True)
    print('Syntaxe OK')
except Exception as e:
    print(f'Erreur: {str(e)[:200]}')
