p='C:/Users/BoulePiou/cockpit-raphael/app.py'
f=open(p,'r',encoding='utf-8')
t=f.read()
f.close()
print('Lignes:', t.count('\n'))
print('Fonctions:', t.count('def '))
