p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()

# Verifier ce qui manque
print('def main present:', 'def main' in t)
print('def page_annexe present:', 'def page_annexe' in t)
print('Derniers 200 caracteres:')
print(repr(t[-200:]))
